const preview_btn = document.querySelector(".preview-article-btn"),
    modal = document.querySelector(".preview-modal"),
    overlay = document.querySelector(".overlay");

const OPEN = "open";

function openModal() {
    console.log("open");
    modal.classList.add(OPEN);
}

function init() {
    preview_btn.addEventListener("click", openModal);
}

init();