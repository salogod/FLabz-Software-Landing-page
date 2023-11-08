document.addEventListener("DOMContentLoaded", function() {
    let currentSlide = 0;
    const slides = document.querySelectorAll(".slide");
    const totalSlides = slides.length;

    const nextBtn = document.querySelector(".next");
    const prevBtn = document.querySelector(".prev");

    function goToSlide(slideNumber) {
        slides[currentSlide].classList.remove("active");
        currentSlide = (slideNumber + totalSlides) % totalSlides; // Esto permite que el slider sea circular
        slides[currentSlide].classList.add("active");
    }

    nextBtn.addEventListener("click", function() {
        goToSlide(currentSlide + 1);
    });

    prevBtn.addEventListener("click", function() {
        goToSlide(currentSlide - 1);
    });

    // Configuración del intervalo para cambiar los slides automáticamente
    let slideInterval = setInterval(function() {
        goToSlide(currentSlide + 1);
    }, 5000);

    // Opcional: Limpia el intervalo cuando el usuario interactúa con los botones
    nextBtn.addEventListener("click", function() {
        clearInterval(slideInterval);
        // Reiniciar el intervalo
        slideInterval = setInterval(function() {
            goToSlide(currentSlide + 1);
        }, 3000);
    });

    prevBtn.addEventListener("click", function() {
        clearInterval(slideInterval);
        // Reiniciar el intervalo
        slideInterval = setInterval(function() {
            goToSlide(currentSlide - 1);
        }, 5000);
    });
});
