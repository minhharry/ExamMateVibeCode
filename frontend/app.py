"""
ExamMate Flask Frontend Application
A modern web interface for the ExamMate API.
"""
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, Response
from dotenv import load_dotenv
from api_client import APIClient
from functools import wraps

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-me')

# Initialize API client
api_base_url = os.getenv('API_BASE_URL', 'http://localhost:8000')
api = APIClient(api_base_url)


def login_required(f):
    """Decorator to require authentication."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'token' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        api.set_token(session['token'])
        return f(*args, **kwargs)
    return decorated_function


def get_api():
    """Get API client with current token."""
    if 'token' in session:
        api.set_token(session['token'])
    return api


# ==================== Authentication Routes ====================

@app.route('/')
def index():
    """Home page - redirect to dashboard or login."""
    if 'token' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            result = api.login(username, password)
            session['token'] = result['access_token']
            api.set_token(result['access_token'])
            user = api.get_current_user()
            session['user'] = user
            flash('Successfully logged in!', 'success')
            return redirect(url_for('dashboard'))
        except Exception as e:
            flash(f'Login failed: {str(e)}', 'error')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        full_name = request.form.get('full_name')
        try:
            api.register(username, password, email, full_name)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Registration failed: {str(e)}', 'error')
    return render_template('register.html')


@app.route('/logout')
def logout():
    """Logout and clear session."""
    session.clear()
    api.clear_token()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


# ==================== Dashboard ====================

@app.route('/dashboard')
@login_required
def dashboard():
    """Main dashboard page."""
    user = session.get('user', {})
    return render_template('dashboard.html', user=user)


# ==================== Documents Routes ====================

@app.route('/documents')
@login_required
def documents():
    """Documents list page."""
    search_query = request.args.get('q', '')
    try:
        if search_query:
            docs = get_api().search_documents(search_query)
        else:
            docs = get_api().get_documents()
    except Exception as e:
        flash(f'Error loading documents: {str(e)}', 'error')
        docs = []
    return render_template('documents.html', documents=docs, search_query=search_query)


@app.route('/documents/upload', methods=['POST'])
@login_required
def upload_document():
    """Upload a document."""
    if 'file' not in request.files:
        flash('No file selected.', 'error')
        return redirect(url_for('documents'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected.', 'error')
        return redirect(url_for('documents'))
    
    try:
        get_api().upload_document((file.filename, file.stream, file.content_type))
        flash('Document uploaded successfully!', 'success')
    except Exception as e:
        flash(f'Upload failed: {str(e)}', 'error')
    return redirect(url_for('documents'))


@app.route('/documents/<doc_id>/download')
@login_required
def download_document(doc_id):
    """Download a document."""
    try:
        response = get_api().download_document(doc_id)
        # Get filename from Content-Disposition header if available
        content_disposition = response.headers.get('Content-Disposition', '')
        filename = 'document.pdf'
        if 'filename=' in content_disposition:
            filename = content_disposition.split('filename=')[-1].strip('"')
        
        return Response(
            response.content,
            headers={
                'Content-Type': response.headers.get('Content-Type', 'application/pdf'),
                'Content-Disposition': f'attachment; filename="{filename}"'
            }
        )
    except Exception as e:
        flash(f'Download failed: {str(e)}', 'error')
        return redirect(url_for('documents'))


@app.route('/documents/<doc_id>/delete', methods=['POST'])
@login_required
def delete_document(doc_id):
    """Delete a document."""
    try:
        get_api().delete_document(doc_id)
        flash('Document deleted successfully!', 'success')
    except Exception as e:
        flash(f'Delete failed: {str(e)}', 'error')
    return redirect(url_for('documents'))


@app.route('/documents/<doc_id>/summary', methods=['POST'])
@login_required
def generate_summary(doc_id):
    """Generate summary for a document."""
    try:
        result = get_api().generate_summary(doc_id)
        flash('Summary generated successfully!', 'success')
    except Exception as e:
        flash(f'Summary generation failed: {str(e)}', 'error')
    return redirect(url_for('documents'))


# ==================== Quizzes Routes ====================

@app.route('/quizzes')
@login_required
def quizzes():
    """Quizzes list page."""
    search_query = request.args.get('q', '')
    try:
        if search_query:
            quiz_list = get_api().search_quizzes(search_query)
        else:
            quiz_list = get_api().get_quizzes()
    except Exception as e:
        flash(f'Error loading quizzes: {str(e)}', 'error')
        quiz_list = []
    
    # Get documents for quiz generation
    try:
        docs = get_api().get_documents()
    except:
        docs = []
    
    return render_template('quizzes.html', quizzes=quiz_list, documents=docs, search_query=search_query)


@app.route('/quizzes/<quiz_id>')
@login_required
def quiz_detail(quiz_id):
    """Quiz detail/taking page."""
    try:
        quiz = get_api().get_quiz(quiz_id)
    except Exception as e:
        flash(f'Error loading quiz: {str(e)}', 'error')
        return redirect(url_for('quizzes'))
    return render_template('quiz_detail.html', quiz=quiz)


@app.route('/quizzes/generate', methods=['POST'])
@login_required
def generate_quiz():
    """Generate a new quiz from a document."""
    document_id = request.form.get('document_id')
    num_questions = int(request.form.get('num_questions', 10))
    try:
        quiz = get_api().generate_quiz(document_id, num_questions)
        flash('Quiz generated successfully!', 'success')
        return redirect(url_for('quiz_detail', quiz_id=quiz['quiz_id']))
    except Exception as e:
        flash(f'Quiz generation failed: {str(e)}', 'error')
    return redirect(url_for('quizzes'))


@app.route('/quizzes/<quiz_id>/delete', methods=['POST'])
@login_required
def delete_quiz(quiz_id):
    """Delete a quiz."""
    try:
        get_api().delete_quiz(quiz_id)
        flash('Quiz deleted successfully!', 'success')
    except Exception as e:
        flash(f'Delete failed: {str(e)}', 'error')
    return redirect(url_for('quizzes'))


# ==================== Schedule Routes ====================

@app.route('/schedule')
@login_required
def schedule():
    """Schedule list page."""
    try:
        schedules = get_api().get_schedules()
    except Exception as e:
        flash(f'Error loading schedules: {str(e)}', 'error')
        schedules = []
    return render_template('schedule.html', schedules=schedules)


@app.route('/schedule/create', methods=['POST'])
@login_required
def create_schedule():
    """Create a new schedule."""
    title = request.form.get('title')
    description = request.form.get('description')
    start_date = request.form.get('start_date') or None
    end_date = request.form.get('end_date') or None
    try:
        get_api().create_schedule(title, description, start_date, end_date)
        flash('Schedule created successfully!', 'success')
    except Exception as e:
        flash(f'Create failed: {str(e)}', 'error')
    return redirect(url_for('schedule'))


@app.route('/schedule/<schedule_id>/update', methods=['POST'])
@login_required
def update_schedule(schedule_id):
    """Update a schedule."""
    title = request.form.get('title')
    description = request.form.get('description')
    start_date = request.form.get('start_date') or None
    end_date = request.form.get('end_date') or None
    try:
        get_api().update_schedule(schedule_id, title, description, start_date, end_date)
        flash('Schedule updated successfully!', 'success')
    except Exception as e:
        flash(f'Update failed: {str(e)}', 'error')
    return redirect(url_for('schedule'))


@app.route('/schedule/<schedule_id>/delete', methods=['POST'])
@login_required
def delete_schedule(schedule_id):
    """Delete a schedule."""
    try:
        get_api().delete_schedule(schedule_id)
        flash('Schedule deleted successfully!', 'success')
    except Exception as e:
        flash(f'Delete failed: {str(e)}', 'error')
    return redirect(url_for('schedule'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
