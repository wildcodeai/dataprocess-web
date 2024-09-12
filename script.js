// Este script está listo para agregar funciones interactivas
document.addEventListener("DOMContentLoaded", function() {
    console.log("Página cargada. Puedes agregar funcionalidades aquí.");
    
    // Ejemplo de animación sencilla (fade-in) al cargar la página
    const images = document.querySelectorAll('.images-grid img');
    images.forEach((img, index) => {
        img.style.opacity = 0;
        setTimeout(() => {
            img.style.transition = 'opacity 0.5s ease-in';
            img.style.opacity = 1;
        }, index * 200);
    });
});
