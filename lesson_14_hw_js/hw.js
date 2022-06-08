const range = document.querySelector('.long')
const bt = document.querySelector('.bt')
var rangWeight = range.offsetWidth

console.log(range.offsetLeft);
console.log(range.offsetWidth);
console.log(bt.clientLeft);
console.log(bt.offsetLeft);

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



