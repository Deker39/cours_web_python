document.getElementById('randBtn').onclick = function(){
    document.querySelector('#randNumber').innerHTML  = Math.floor(Math.random()*100)
}

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
