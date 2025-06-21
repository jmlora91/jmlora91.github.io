async function loadData() {
    const res = await fetch('data.json');
    return res.json();
}

function createMenu(menuItems) {
    const menu = document.getElementById('menu');
    menu.innerHTML = '';

    menuItems.forEach(item => {
        if (item.id === 'toggle-theme') {
            const link = document.createElement('a');
            link.href = '#';
            link.textContent = item.label;
            link.classList.add('toggle-theme');
            link.addEventListener('click', (e) => {
                e.preventDefault();
                toggleTheme();
            });
            menu.appendChild(link);
            return;
        }

        const link = document.createElement('a');
        link.href = `#section-${item.id}`;
        link.textContent = item.label;
        link.dataset.section = item.id;

        link.addEventListener('click', () => {
            scrollToSection(item.id);
            closeMenuMobile();
            setActiveMenuLink(item.id);
        });

        menu.appendChild(link);
    });
}

function setActiveMenuLink(sectionId) {
    const links = document.querySelectorAll('#menu a:not(.toggle-theme)');
    links.forEach(link => link.classList.toggle('active', link.dataset.section === sectionId));
}

function scrollToSection(sectionId) {
    const sectionEl = document.getElementById(`section-${sectionId}`);
    if (sectionEl) {
        sectionEl.scrollIntoView({ behavior: 'smooth' });
    }
}

function renderSections(sections) {
    const content = document.getElementById('content');
    content.innerHTML = '';

    for (const [id, section] of Object.entries(sections)) {
        if (id === 'footer') continue;

        let sectionHtml = '';

        if (section.skillsList && Array.isArray(section.skillsList)) {
            let skillsHtml = '';
            section.skillsList.forEach(skill => {
                skillsHtml += `
                    <div class="skill">
                        <span class="skill-name">${skill.name}</span>
                        <div class="skill-bar"><div class="skill-level" style="width: ${skill.level}%;"></div></div>
                    </div>`;
            });

            sectionHtml = `
                <div class="content-section hidden" id="section-${id}">
                    <h1>${section.title}</h1>
                    <div class="skills-container">${skillsHtml}</div>
                </div>
            `;
        } else {
            sectionHtml = `
                <div class="content-section hidden" id="section-${id}">
                    <h1>${section.title}</h1>
                    ${section.content}
                </div>
            `;
        }

        content.insertAdjacentHTML('beforeend', sectionHtml);
    }

    setupContactForm();
}

function setupContactForm() {
    const form = document.getElementById('contact-form');
    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            const name = form.name.value.trim();
            const email = form.email.value.trim();
            const message = form.message.value.trim();
            const response = document.getElementById('form-response');

            if (name && email && message) {
                response.textContent = 'Mensaje enviado con éxito. (Simulación)';
                response.style.color = 'green';
                form.reset();
            } else {
                response.textContent = 'Por favor, rellena todos los campos.';
                response.style.color = 'red';
            }
        });
    }
}

function loadFooter() {
    const footer = document.getElementById('footer');
    footer.textContent = window.appData.sections.footer.content;
}

function toggleTheme() {
    document.body.classList.toggle('dark');
    if (document.body.classList.contains('dark')) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.removeItem('theme');
    }
}

function applySavedTheme() {
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark');
    }
}

function toggleMenuMobile() {
    const menu = document.getElementById('menu');
    menu.classList.toggle('open');
}

function closeMenuMobile() {
    const menu = document.getElementById('menu');
    menu.classList.remove('open');
}

document.getElementById('menu-toggle').addEventListener('click', toggleMenuMobile);

// Actualizar enlace activo al hacer scroll
window.addEventListener('scroll', () => {
    const sections = Object.keys(window.appData.sections).filter(id => id !== 'footer');
    let currentSectionId = sections[0];

    for (const id of sections) {
        const sectionEl = document.getElementById(`section-${id}`);
        if (sectionEl) {
            const rect = sectionEl.getBoundingClientRect();
            if (rect.top <= window.innerHeight / 3) {
                currentSectionId = id;
            }
        }
    }

    setActiveMenuLink(currentSectionId);
    updateScrollProgress();
});

// Animaciones scroll reversibles
function setupScrollAnimations() {
    const sections = document.querySelectorAll('.content-section');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
            } else {
                entry.target.classList.remove('show');
            }
        });
    }, { threshold: 0.1 });

    sections.forEach(section => observer.observe(section));
}

// Loader animado
function hideLoader() {
    const loader = document.getElementById('loader');
    if (loader) {
        loader.style.opacity = '0';
        setTimeout(() => loader.style.display = 'none', 500);
    }
}

// Scroll progress bar
function updateScrollProgress() {
    const scrollTop = window.scrollY;
    const docHeight = document.body.scrollHeight - window.innerHeight;
    const progress = (scrollTop / docHeight) * 100;
    const progressBar = document.getElementById('scroll-progress');
    if (progressBar) {
        progressBar.style.width = `${progress}%`;
    }
}

async function init() {
    window.appData = await loadData();
    createMenu(window.appData.menu);
    renderSections(window.appData.sections);
    loadFooter();
    applySavedTheme();
    setActiveMenuLink(window.appData.menu[0].id);
    setupScrollAnimations();
    hideLoader();
}

init();
