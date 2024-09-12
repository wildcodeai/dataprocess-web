// Seleccionar todos los botones de pestañas
const tabButtons = document.querySelectorAll('.tab-button');

// Añadir un evento de clic a cada botón
tabButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remover la clase "active" de todos los botones
        tabButtons.forEach(btn => btn.classList.remove('active'));
        
        // Añadir la clase "active" al botón que se ha clicado
        button.classList.add('active');
        
        // Seleccionar todas las secciones de contenido
        const tabContents = document.querySelectorAll('.tab-content');
        
        // Remover la clase "active" de todas las secciones
        tabContents.forEach(content => content.classList.remove('active'));
        
        // Mostrar el contenido asociado con el botón clicado
        const tabId = button.getAttribute('data-tab');
        document.getElementById(tabId).classList.add('active');
    });
});
