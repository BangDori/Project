function loadImage() {
    let input = document.createElement("input");

    input.type = "file";
    input.accept = "image/png, image/gif, image/jpeg";

    input.onchange = function (e) {
        document.querySelector(".write-content");

        let selectFile = document.querySelector("#inputImage").files[0];
        const file = URL.createObjectURL(selectFile);
        document.querySelector(".write-content").src = file;
    }

    input.click();
}

function leftAlign() {
    document.querySelector(".write-content").style.textAlign="left";
    document.getElementsByName("alignStatus").value = "left";
}

function middleAlign() {
    document.querySelector(".write-content").style.textAlign="center";
    document.getElementsByName("alignStatus").value = "center";
}

function rightAlign() {
    document.querySelector(".write-content").style.textAlign="right";
    document.getElementsByName("alignStatus").value = "right";
}