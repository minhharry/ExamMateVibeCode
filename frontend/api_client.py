"""
API Client for ExamMate Backend
Wraps all backend API endpoints with proper authentication handling.
"""
import requests
from typing import Optional, List, Dict, Any


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.token: Optional[str] = None

    def set_token(self, token: str):
        """Set the authentication token."""
        self.token = token

    def clear_token(self):
        """Clear the authentication token."""
        self.token = None

    def _headers(self) -> Dict[str, str]:
        """Get headers with authorization if token is set."""
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make a request to the API."""
        url = f"{self.base_url}{endpoint}"
        if "headers" not in kwargs:
            kwargs["headers"] = self._headers()
        return requests.request(method, url, **kwargs)

    # ==================== Authentication ====================

    def register(self, username: str, password: str, email: str = None, full_name: str = None) -> Dict[str, Any]:
        """Register a new user."""
        data = {"username": username, "password": password}
        if email:
            data["email"] = email
        if full_name:
            data["full_name"] = full_name
        response = self._request("POST", "/register", json=data)
        response.raise_for_status()
        return response.json()

    def login(self, username: str, password: str) -> Dict[str, Any]:
        """Login and get access token."""
        response = self._request(
            "POST",
            "/token",
            data={"username": username, "password": password},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        response.raise_for_status()
        return response.json()

    def get_current_user(self) -> Dict[str, Any]:
        """Get current user info."""
        response = self._request("GET", "/users/me/")
        response.raise_for_status()
        return response.json()

    def update_language(self, language: str) -> Dict[str, Any]:
        """Update user's language preference."""
        response = self._request("PUT", f"/users/me/language?language={language}")
        response.raise_for_status()
        return response.json()

    # ==================== Documents ====================

    def get_documents(self) -> List[Dict[str, Any]]:
        """Get all documents."""
        response = self._request("GET", "/documents")
        response.raise_for_status()
        return response.json()

    def search_documents(self, query: str) -> List[Dict[str, Any]]:
        """Search documents."""
        response = self._request("GET", f"/documents/search?q={query}")
        response.raise_for_status()
        return response.json()

    def get_document(self, doc_id: str) -> Dict[str, Any]:
        """Get a specific document."""
        response = self._request("GET", f"/documents/{doc_id}")
        response.raise_for_status()
        return response.json()

    def upload_document(self, file) -> Dict[str, Any]:
        """Upload a document."""
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        response = requests.post(
            f"{self.base_url}/documents",
            files={"file": file},
            headers=headers
        )
        response.raise_for_status()
        return response.json()

    def delete_document(self, doc_id: str) -> Dict[str, Any]:
        """Delete a document."""
        response = self._request("DELETE", f"/documents/{doc_id}")
        response.raise_for_status()
        return response.json() if response.text else {}

    def download_document(self, doc_id: str) -> requests.Response:
        """Download a document."""
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return requests.get(
            f"{self.base_url}/documents/{doc_id}/download",
            headers=headers,
            stream=True
        )

    def generate_summary(self, doc_id: str) -> Dict[str, Any]:
        """Generate summary for a document."""
        response = self._request("POST", f"/documents/{doc_id}/summary")
        response.raise_for_status()
        return response.json() if response.text else {}

    # ==================== Quizzes ====================

    def get_quizzes(self) -> List[Dict[str, Any]]:
        """Get all quizzes."""
        response = self._request("GET", "/quizzes")
        response.raise_for_status()
        return response.json()

    def search_quizzes(self, query: str) -> List[Dict[str, Any]]:
        """Search quizzes."""
        response = self._request("GET", f"/quizzes/search?q={query}")
        response.raise_for_status()
        return response.json()

    def get_quiz(self, quiz_id: str) -> Dict[str, Any]:
        """Get a specific quiz with questions."""
        response = self._request("GET", f"/quizzes/{quiz_id}")
        response.raise_for_status()
        return response.json()

    def generate_quiz(self, document_id: str, num_questions: int = 10) -> Dict[str, Any]:
        """Generate a quiz from a document."""
        response = self._request(
            "POST",
            "/quizzes/generate",
            json={"document_id": document_id, "num_questions": num_questions}
        )
        response.raise_for_status()
        return response.json()

    def delete_quiz(self, quiz_id: str) -> Dict[str, Any]:
        """Delete a quiz."""
        response = self._request("DELETE", f"/quizzes/{quiz_id}")
        response.raise_for_status()
        return response.json() if response.text else {}

    # ==================== Schedule ====================

    def get_schedules(self) -> List[Dict[str, Any]]:
        """Get all schedules."""
        response = self._request("GET", "/schedule")
        response.raise_for_status()
        return response.json()

    def get_schedule(self, schedule_id: str) -> Dict[str, Any]:
        """Get a specific schedule."""
        response = self._request("GET", f"/schedule/{schedule_id}")
        response.raise_for_status()
        return response.json()

    def create_schedule(self, title: str, description: str, start_date: str = None, end_date: str = None) -> Dict[str, Any]:
        """Create a new schedule."""
        data = {"title": title, "description": description}
        if start_date:
            data["start_date"] = start_date
        if end_date:
            data["end_date"] = end_date
        response = self._request("POST", "/schedule", json=data)
        response.raise_for_status()
        return response.json()

    def update_schedule(self, schedule_id: str, title: str, description: str, start_date: str = None, end_date: str = None) -> Dict[str, Any]:
        """Update a schedule."""
        data = {"title": title, "description": description}
        if start_date:
            data["start_date"] = start_date
        if end_date:
            data["end_date"] = end_date
        response = self._request("PUT", f"/schedule/{schedule_id}", json=data)
        response.raise_for_status()
        return response.json()

    def delete_schedule(self, schedule_id: str) -> Dict[str, Any]:
        """Delete a schedule."""
        response = self._request("DELETE", f"/schedule/{schedule_id}")
        response.raise_for_status()
        return response.json() if response.text else {}

    # ==================== Health ====================

    def health_check(self) -> Dict[str, Any]:
        """Check API health."""
        response = requests.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json() if response.text else {"status": "ok"}
