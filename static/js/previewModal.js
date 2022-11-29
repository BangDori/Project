const preview_btn = document.querySelector(".preview-article-btn"),
    modal = document.querySelector(".preview-modal"),
    overlay = document.querySelector(".overlay");

const OPEN = "open";

function openModal() {
    modal.classList.add(OPEN);
    overlay.classList.add(OPEN);
}

function closeModal() {
    modal.classList.remove(OPEN);
    overlay.classList.remove(OPEN);
}

function init() {
    preview_btn.addEventListener("click", openModal);
}

init();