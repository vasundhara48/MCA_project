document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            navbar.classList.toggle('scrolled', window.scrollY > 50);
        });
    }

    // Scroll Reveal animation
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const delay = entry.target.getAttribute('data-delay') || 0;
                setTimeout(() => entry.target.classList.add('active'), parseInt(delay));
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    revealElements.forEach(el => revealObserver.observe(el));

    // Hero animation delay
    document.querySelectorAll('.anim-item').forEach(item => {
        const delay = item.getAttribute('data-delay') || 0;
        item.style.animationDelay = `${delay}ms`;
    });

    // Skill Search Autocomplete
    const skillInput = document.getElementById('skill-input');
    const suggestionsBox = document.getElementById('skill-suggestions');
    
    if (skillInput && suggestionsBox && typeof allSkills !== 'undefined') {
        skillInput.addEventListener('input', function() {
            const val = this.value.toLowerCase().trim();
            suggestionsBox.innerHTML = '';
            
            if (val.length < 1) {
                suggestionsBox.classList.remove('open');
                return;
            }
            
            const filtered = allSkills.filter(s => s.toLowerCase().includes(val)).slice(0, 8);
            if (filtered.length === 0) {
                suggestionsBox.classList.remove('open');
                return;
            }
            
            filtered.forEach(skill => {
                const div = document.createElement('div');
                div.className = 'suggestion-item';
                div.textContent = skill;
                div.addEventListener('click', () => {
                    skillInput.value = skill;
                    suggestionsBox.classList.remove('open');
                });
                suggestionsBox.appendChild(div);
            });
            
            suggestionsBox.classList.add('open');
        });
        
        document.addEventListener('click', function(e) {
            if (!skillInput.contains(e.target) && !suggestionsBox.contains(e.target)) {
                suggestionsBox.classList.remove('open');
            }
        });
    }

    // Skill Browser Toggle
    const browserToggle = document.getElementById('browser-toggle');
    const browserPanel = document.getElementById('browser-panel');
    if (browserToggle && browserPanel) {
        browserToggle.addEventListener('click', function() {
            this.classList.toggle('open');
            browserPanel.classList.toggle('open');
        });
    }

    // Role description dynamic update
    const roleSelect = document.getElementById('role-select');
    const roleDescription = document.getElementById('role-description');
    if (roleSelect && roleDescription && typeof rolesData !== 'undefined') {
        const initialRole = roleSelect.value;
        if (initialRole && rolesData[initialRole]) {
            roleDescription.textContent = rolesData[initialRole].description;
        } else if (!initialRole) {
            roleDescription.textContent = 'Select a role to see its description.';
        }
        
        roleSelect.addEventListener('change', function() {
            const selectedRole = this.value;
            if (selectedRole && rolesData[selectedRole]) {
                roleDescription.textContent = rolesData[selectedRole].description;
            } else {
                roleDescription.textContent = 'Select a role to see its description.';
            }
        });
    }
    
    // Auto-hide toast messages
    const messagesContainer = document.getElementById('messages-container');
    if (messagesContainer) {
        setTimeout(() => {
            messagesContainer.style.transition = 'opacity 0.5s ease';
            messagesContainer.style.opacity = '0';
            setTimeout(() => messagesContainer.remove(), 500);
        }, 4000);
    }
});