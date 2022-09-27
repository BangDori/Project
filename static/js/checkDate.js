const dates = document.querySelectorAll(".js-date");

function checkNow() {
    
}

function changeDate() {
    dates.forEach(date => {
        console.log(date);
    })
}

function init() {
    changeDate();
}

init();