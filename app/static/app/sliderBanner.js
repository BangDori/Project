const directions = document.querySelectorAll(".direction-move"),
    banner_content = document.querySelector(".banner-content"),
    banner = document.querySelector(".banner"),
    banner_count = document.querySelector(".banner-count");

const SHOWING = "showing",
    PREV_MOVING = "js-prev",
    NEXT_MOVING = "js-next",
    CLICKED_BANNER = "js-clicked-count";

let mode = 'auto';

function handleDirection() {
    directions.forEach(direction => {
        direction.addEventListener("click", (event) => {
            const current_slide = banner_content.querySelector(`.${SHOWING}`);
            const current_count = banner_count.querySelector(`.${CLICKED_BANNER}`);
            mode = 'click';

            if(event.target.name === 'left') {
                if(current_slide.previousElementSibling === null) return;
                handleLeft(current_slide, current_count);
            } else if(event.target.name === 'right')  {
                if(current_slide.nextElementSibling === null) return;
                handleRight(current_slide, current_count);
            }
        });
    })
}

function handleLeft(current_slide, current_count) {
    const prev_slide = current_slide.previousElementSibling;
    const prev_count = current_count.previousElementSibling;

    prev_slide.classList.remove(PREV_MOVING);
    prev_slide.classList.add(SHOWING);
    prev_count.classList.add(CLICKED_BANNER);

    current_slide.classList.remove(SHOWING);
    current_slide.classList.add(NEXT_MOVING);
    current_count.classList.remove(CLICKED_BANNER);
}

function handleRight(current_slide, current_count) {
    const next_slide = current_slide.nextElementSibling;
    const next_count = current_count.nextElementSibling;

    if(next_slide.nextElementSibling === null) {
        mode = 'stop';
        return;
    }

    next_slide.classList.add(SHOWING);
    next_slide.classList.remove(NEXT_MOVING);
    next_count.classList.add(CLICKED_BANNER);

    current_slide.classList.remove(SHOWING);
    current_slide.classList.add(PREV_MOVING);
    current_count.classList.remove(CLICKED_BANNER);
}

function autoDirection() {
    let timer = setInterval(function () {
        console.log(mode);
        if(mode === 'click') {
            mode = 'auto';
        } else if(mode == 'auto') {
            handleRight(banner_content.querySelector(`.${SHOWING}`), banner_count.querySelector(`.${CLICKED_BANNER}`));
        } else if(mode == 'stop') {
            clearInterval(timer);
        }
    }, 3000)
}

function init() {
    handleDirection();
    autoDirection();
}

init();