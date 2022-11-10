console.log("H");



function changeNone() {
var consist = document.querySelectorAll('.content');
var index = document.querySelectorAll('.index-list');
                    var i = 0;
                    while(i < consist.length){
                        consist[i].style.display = 'none';
                        index[i].style.backgroundColor='white';
                        index[i].style.color='black';
                        i = i+1;
                    }
}


function changeInfo(){
                    changeNone();
                    document.querySelector('#myinfo-box').style.display = 'block';
                    document.querySelector('#myinfo-list').style.backgroundColor ='green';
                    document.querySelector('#myinfo-list').style.color ='white';


}

function changePost(){
                    changeNone();
                    document.querySelector('#mypost-box').style.display = 'block';
                    document.querySelector('#mynotice-list').style.backgroundColor ='green';
                    document.querySelector('#mynotice-list').style.color ='white';


}

function changeBookmark(){
                    changeNone();
                    document.querySelector('#bookmark-box').style.display = 'block';
                    document.querySelector('#bookmark-list').style.backgroundColor ='green';
                    document.querySelector('#bookmark-list').style.color ='white';
}

function changeSet(){
                    changeNone();
                    document.querySelector('#set-box').style.display = 'block';
                    document.querySelector('#set-list').style.backgroundColor ='green';
                    document.querySelector('#set-list').style.color ='white';

}


