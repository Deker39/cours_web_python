document.getElementById('randBtn').onclick = function(){
    document.querySelector('#randNumber').innerHTML  = Math.floor(Math.random()*100)
}
/*-------------------------------------------------*/
var xy = document.createElement('h5')
var mouseClick = document.createElement('h5')
var sect = document.querySelector('#srceen')
sect.appendChild(xy)
sect.appendChild(mouseClick)

document.body.oncontextmenu = function(){ return false}

sect.onclick = function(){
    mouseClick.innerHTML = 'Click left mouse button'
}
sect.oncontextmenu = function(){
    mouseClick.innerHTML = 'Click rigth mouse button'
}
sect.onmousemove = function(event){
    xy.innerHTML = `x = ${event.clientX} ,y = ${event.clientY}`
}
/*-------------------------------------------------*/
function btnHide(){
    var text = document.querySelector('#text')
    if(text.style.display == 'block'){
        text.style.display = 'none'
        document.querySelector('#hide').innerHTML = 'Show text'
    }else{
        text.style.display = 'block'
        document.querySelector('#hide').innerHTML = 'Hide'
    }
    
    
}
/*-------------------------------------------------*/
function openCity(e, cityName) {
    var i, 
    tabcontent, 
    tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    tablinks = document.getElementsByClassName("tablinks");

    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("active", "");
    }
    
    document.getElementById(cityName).style.display = "block";
    e.currentTarget.className += "active";
}

window.onload = function() {
    openCity(event,'html');
    document.querySelector('#first').classList.add('active')
  };

/*-------------------------------------------------*/
removes  = document.querySelectorAll('#remove')
list = document.querySelector('#listIpsum')

for (i = 0; i < list.children.length; i++){
    removes[i].onclick = function(){
        this.parentNode.remove()
    }
}


/*-------------------------------------------------*/
var width = 0;
var i = 0;
document.getElementById('add').onclick = function(){
    var elem = document.querySelector('.progress-bar');
    if (width >= 100) {

    } else {
    width += 5;
    elem.style.width = width + "%";
    elem.innerHTML = width  + "%";
    }
    

}

