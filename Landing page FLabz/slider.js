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
});
