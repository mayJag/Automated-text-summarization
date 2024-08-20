document.addEventListener('DOMContentLoaded', function() {
    // Example: Simple form validation
    const form = document.querySelector('form');
    const textarea = document.querySelector('textarea');

    form.addEventListener('submit', function(event) {
        if (textarea.value.trim() === '') {
            event.preventDefault();
            alert('Please enter some text to summarize.');
            textarea.focus();
        }
    });

    // Example: Adding some interactivity or animation (e.g., focus effect)
    textarea.addEventListener('focus', function() {
        this.style.backgroundColor = '#e9f5ff';
    });

    textarea.addEventListener('blur', function() {
        this.style.backgroundColor = '';
    });

    // Example: Smooth scroll effect for anchor links (if any)
    const scrollLinks = document.querySelectorAll('a[href^="#"]');
    scrollLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
});
