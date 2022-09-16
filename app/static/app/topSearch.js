const body = document.querySelector("body"),
  top_search = body.querySelector(".top-search-form");

const SHOWING_BOARD = "showing-board";

function handleClick(event) {
  console.log(event.target);

  if (event.target.classList.contains("top-search-keyword")) {
    top_search.classList.add(SHOWING_BOARD);
  } else {
    top_search.classList.remove(SHOWING_BOARD);
  }
}

function init() {
  body.addEventListener("click", handleClick);
}

init();
