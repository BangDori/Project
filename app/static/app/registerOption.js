const email_box = document.querySelector("#emailBox"),
    year_box = document.querySelector("#yearBox"),
    month_box = document.querySelector("#monthBox"),
    day_box = document.querySelector("#dayBox"),
    select_email_box = document.querySelector(".select-email-box"),
    input_email_box = document.querySelector(".input-email-box");

const DIRECT = "hidden";

function setAddress() {
    let option;
    let addres = [
        {value: 'naver.com', register_user_email: 'naver.com'},
        {value: 'daum.com', register_user_email: 'daum.com'},
        {value: 'google.com', register_user_email: 'google.com'},
        {value: 'direct', register_user_email: '직접 입력'},
    ];

    addres.unshift({value: '', register_user_email: '주소 입력'});

    for(const addr of addres) {
        let option = document.createElement("option");
        option.value = addr.value;
        option.innerText = addr.register_user_email;
        email_box.appendChild(option);
    }
}

function setBirth() {
    let option;

    for(let i = 1970; i <= 2022; i++) {
        option = document.createElement("option");
        option.innerText = i;
        year_box.appendChild(option);
    }
    for(let i = 1; i <= 12; i++) {
        option = document.createElement("option");
        option.innerText = i;
        month_box.appendChild(option);
    }
    for(let i = 1; i <= 31; i++) {
        option = document.createElement("option");
        option.innerText = i;
        day_box.appendChild(option);
    }
}

function changeEmail(event) {
    console.log(event.target.value);

    if(event.target.value === 'direct') {
        console.log("yes");
        select_email_box.innerText = "";


        select_email_box.classList.add(DIRECT);
        input_email_box.classList.remove(DIRECT);

    } else {
        input_email_box.value = "";

        input_email_box.classList.add(DIRECT);
        select_email_box.classList.remove(DIRECT);

        select_email_box.innerText = event.target.value;
    }
}

function init() {
    setAddress();
    setBirth();
    email_box.addEventListener("change", changeEmail);
}

init();