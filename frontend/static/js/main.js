/**
 * ExamMate Frontend JavaScript
 * Handles modals, form interactions, and UI enhancements
 */

// ==================== Modal Functions ====================

/**
 * Toggle modal visibility
 * @param {string} modalId - ID of the modal to toggle
 */
function toggleModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.toggle('active');

        // Prevent body scroll when modal is open
        if (modal.classList.contains('active')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    }
}

// Close modal when clicking outside
document.addEventListener('click', function (e) {
    if (e.target.classList.contains('modal')) {
        e.target.classList.remove('active');
        document.body.style.overflow = '';
    }
});

// Close modal with Escape key
document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        const activeModal = document.querySelector('.modal.active');
        if (activeModal) {
            activeModal.classList.remove('active');
            document.body.style.overflow = '';
        }
    }
});

// ==================== Flash Messages ====================

// Auto-dismiss flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function () {
    const flashMessages = document.querySelectorAll('.flash');
    flashMessages.forEach(function (flash) {
        setTimeout(function () {
            flash.style.opacity = '0';
            flash.style.transform = 'translateY(-10px)';
            setTimeout(function () {
                flash.remove();
            }, 300);
        }, 5000);
    });
});

// ==================== Form Enhancements ====================

// Add loading state to forms on submit
document.addEventListener('DOMContentLoaded', function () {
    const forms = document.querySelectorAll('form');
    forms.forEach(function (form) {
        form.addEventListener('submit', function () {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn && !submitBtn.disabled) {
                submitBtn.disabled = true;
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<span class="loading-spinner"></span> Loading...';

                // Re-enable after timeout (in case of error)
                setTimeout(function () {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalText;
                }, 10000);
            }
        });
    });
});

// ==================== Animations ====================

// Animate elements on scroll
document.addEventListener('DOMContentLoaded', function () {
    const animateOnScroll = function () {
        const elements = document.querySelectorAll('.glass-card');
        elements.forEach(function (el) {
            const rect = el.getBoundingClientRect();
            const isVisible = rect.top < window.innerHeight - 100;
            if (isVisible) {
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }
        });
    };

    // Initial check
    animateOnScroll();

    // Check on scroll
    window.addEventListener('scroll', animateOnScroll, { passive: true });
});

// ==================== File Upload Preview ====================

// Show selected filename for file inputs
document.addEventListener('DOMContentLoaded', function () {
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(function (input) {
        input.addEventListener('change', function () {
            const label = input.parentElement.querySelector('label');
            if (label && input.files.length > 0) {
                const originalText = label.textContent;
                label.textContent = input.files[0].name;
                label.title = 'Click to change file';
            }
        });
    });
});

// ==================== Utility Functions ====================

/**
 * Format date string for display
 * @param {string} dateString - ISO date string
 * @returns {string} Formatted date
 */
function formatDate(dateString) {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

/**
 * Copy text to clipboard
 * @param {string} text - Text to copy
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function () {
        showToast('Copied to clipboard!', 'success');
    }).catch(function (err) {
        console.error('Failed to copy:', err);
    });
}

/**
 * Show toast notification
 * @param {string} message - Message to display
 * @param {string} type - Toast type (success, error, warning, info)
 */
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `flash flash-${type}`;
    toast.innerHTML = `
        ${message}
        <button class="flash-close" onclick="this.parentElement.remove()">×</button>
    `;

    const container = document.querySelector('.flash-messages') ||
        document.querySelector('.main-content');

    if (container) {
        container.insertBefore(toast, container.firstChild);

        // Auto-remove after 5 seconds
        setTimeout(function () {
            toast.style.opacity = '0';
            setTimeout(function () {
                toast.remove();
            }, 300);
        }, 5000);
    }
}

// ==================== Keyboard Navigation ====================

// Enable keyboard navigation for option buttons
document.addEventListener('keydown', function (e) {
    if (e.target.classList.contains('option-btn')) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            e.target.click();
        }
    }
});
