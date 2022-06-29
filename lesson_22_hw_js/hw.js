const range = document.querySelector('.long')
const bt = document.querySelector('.bt')
var rangWeight = range.offsetWidth

const initResize = e => {
    e.preventDefault;
    pos2 = e.clientX;
    window.addEventListener("mousemove", startResize);
    window.addEventListener("mouseup", stopResize);
  };
const startResize = e => {
    pos1 = pos2 - e.clientX;
    pos2 = e.clientX;
    if((bt.offsetLeft -  pos1) <= 0) bt.style.left  = 0 , pos1 = 0
    if((bt.offsetLeft -  pos1) >= (range.offsetWidth-25)) bt.style.right  = 0,  pos1 = 0
    else bt.style.left = (bt.offsetLeft -  pos1) + "px";
    
    }
const stopResize = e => {
        window.removeEventListener('mousemove', startResize);
        window.removeEventListener('mouseup', stopResize);
      };
bt.addEventListener("mousedown", initResize);

/*----------------------------------------------------------*/

let imgArray = ['img/github.svg.png','img/HTML5.svg.png','img/javascrip.png','img/python.png']
let vievImage = document.querySelector('#img')
vievImage.style.padding = "25px"
console.log(imgArray.length);
var i = 0

function right(){
    vievImage.setAttribute('src',imgArray[i++])
    vievImage.style.visibility = "visible"
    if( i ==  imgArray.length )  i = imgArray.length - 1  
}

function left(){
    if(i <= 0){vievImage.style.visibility = "hidden"}
    else{
        vievImage.setAttribute('src',imgArray[--i])
        vievImage.style.visibility = "visible"
        if( i <= 0)  i = 1
    }
 
    
}


