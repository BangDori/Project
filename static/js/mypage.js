function changeNone() {
var consist = document.querySelectorAll('.content');
var index = document.querySelectorAll('.index-list');
                    var i = 0;
                    while(i < consist.length){
                        index[i].style.backgroundColor='white';
                        index[i].style.color='black';
                        i = i+1;
                    }
}


function changeInfo(){
                    changeNone();
                    document.querySelector('#myinfo-list').style.backgroundColor ='green';
                    document.querySelector('#myinfo-list').style.color ='white';


}

function changePost(){
                    changeNone();
                    document.querySelector('#mynotice-list').style.backgroundColor ='green';
                    document.querySelector('#mynotice-list').style.color ='white';


}

function changeBookmark(){
                    changeNone();
                    document.querySelector('#bookmark-list').style.backgroundColor ='green';
                    document.querySelector('#bookmark-list').style.color ='white';
}

function changeAddress(){
                    changeNone();
                    document.querySelector('#address-list').style.backgroundColor ='green';
                    document.querySelector('#address-list').style.color ='white';
}

function changeCorporate(){
                    changeNone();
                    document.querySelector('#corporate-list').style.backgroundColor ='green';
                    document.querySelector('#corporate-list').style.color ='white';
}



