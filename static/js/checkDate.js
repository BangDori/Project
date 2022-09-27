const dates = document.querySelectorAll(".js-date");

function checkNow() {
    const now = new Date();
    const year = now.getFullYear();
    const month = now.getMonth();
    const day = now.getDate();

    console.log(now);
    console.log(year, month+1, day);

    board_date = checkBoardDate();
}

function checkBoardDate() {
    const now = new Date();

    dates.forEach(date => {
        const tmp = date.innerHTML.split(/[년|월|일| ]/);
        const board_time = tmp.filter(i => {
            return i !== '';
        }) 

        console.log(board_time);
        // console.log(a[3])
        if(now.getFullYear() > parseInt(board_time[0])) {
            date.innerHTML = `${now.getFullYear() - parseInt(board_time[0])}년 전`;
        } else if(now.getMonth() > parseInt(board_time[1])) {
            date.innerHTML = `${now.getMonth() - parseInt(board_time[1])}달 전`
        } else if(now.getDate() > parseInt(board_time[2])) {
            date.innerHTML = `${now.getDate() - parseInt(board_time[2])}일 전`
        } else {
            if(board_time[4] === '오전') {
                date.innerHTML = board_time[3];
            } else {
                const t = board_time[3].split(':');
                t[0] = `${parseInt(t[0]) + 12}`;
                board_time[3] = t.join(":");
                console.log(board_time[3]);
                date.innerHTML = board_time[3];
                // const t = a[4].split(':');
                // console.log(t);
                // date.innerHTML = 
            }
        }
    })

}

function init() {
    checkNow();
}

init();