document.addEventListener('DOMContentLoaded', function() {
    const slideShow = document.getElementById("slideShow");
    const images = slideShow.querySelectorAll("img");
    const prevBtn = document.getElementById("prevBtn");
    const nextBtn = document.getElementById("nextBtn");
    const currentSlide = document.getElementById("currentSlide");

    let currentIndex = 0;

    // Показать первое изображение
    showCurrentImage();

    // Обработчик кнопки "Вперёд"
    nextBtn.addEventListener("click", () => {
        currentIndex++;
        if (currentIndex > images.length - 1) {
            currentIndex = 0;
        }
        showCurrentImage();
    });

    // Обработчик кнопки "Назад"
    prevBtn.addEventListener("click", () => {
        currentIndex--;
        if (currentIndex < 0) {
            currentIndex = images.length - 1;
        }
        showCurrentImage();
    });

    // Функция для показа текущей картинки
    function showCurrentImage() {
        for (let i = 0; i < images.length; i++) {
            images[i].classList.remove("active");
            images[i].classList.add("inactive");
        }

        images[currentIndex].classList.remove("inactive");
        images[currentIndex].classList.add("active");

        currentSlide.textContent = `Изображение ${currentIndex + 1} из ${images.length}`;
    }
});