/*-------------------------------------------------*/

var ul = document.querySelectorAll('#first .list-group a:is([href^="https://"])')
ul.forEach(function(el){
    el.style.color = 'green'
    el.style.borderBottom = "2px dashed green"
})

/*-------------------------------------------------*/
var first_list = document.getElementById('first_list')

first_list.addEventListener('click',function(e) {
    e.target.children[0].classList.toggle('display-block')
})
first_list.addEventListener('mouseover',function(e) {
    e.target.classList.add('bold')
})
first_list.addEventListener('mouseout',function(e) {
    e.target.classList.remove('bold')
})

/*-------------------------------------------------*/
let third_list = document.getElementById('bookList')
let ctrl_v  
let mouse_v  
let shift_v  


third_list.addEventListener('click',function(e) {
    if(e.ctrlKey){
        ctrl_v = [].indexOf.call(this.children, (e ? e.target : event.srcElement)  )

       
    }else{
        document.querySelectorAll('#bookList li.list-group-item-warning').forEach(function (el) {
            el.classList.remove('list-group-item-warning');
        });
    }
    if(e.shiftKey){
        shift_v = [].indexOf.call(this.children, (e ? e.target : event.srcElement)  )
        let min = Math.min(ctrl_v,mouse_v)
        let max = Math.max(ctrl_v,mouse_v)
        if(shift_v > min){
            for(var i = min; i < shift_v;i++){
                this.getElementsByTagName('li')[i].classList.add('list-group-item-warning')
            }
           
        }else{
            for(var i = shift_v; i <= max;i++){
                this.getElementsByTagName('li')[i].classList.add('list-group-item-warning')
            }
        }
    }
    if(!e.keydown){
        e.target.classList.toggle('list-group-item-warning')
        mouse_v   = [].indexOf.call(this.children, (e ? e.target : event.srcElement)  )
    }
  
})
/*-------------------------------------------------*/

document.body.addEventListener("keydown", keyPress);
 
function keyPress(e) {
    if ((e.code === "KeyS" || e.code === "KeyE") && e.ctrlKey) {
        e.preventDefault();
        let el = document.querySelector("hr").nextElementSibling;
        if (e.code === "KeyS" && el.nodeName === "TEXTAREA") {
            let newEl = document.createElement("div");
            newEl.textContent = el.value; 
            el.replaceWith(newEl);
        }
        else if (e.code === "KeyE" && el.nodeName === "DIV") {
            let newEl = document.createElement("textarea");
            newEl.textContent = el.textContent;
            newEl.classList.add('area') 
            el.replaceWith(newEl);
        }
    }
}

/*-------------------------------------------------*/

function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("content__table");
    switching = true;
    dir = "asc";

    while (switching) {   
      switching = false;
      rows = table.getElementsByTagName("TR");
      for (i = 1; i < (rows.length - 1); i++) {
       shouldSwitch = false; 
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];
        if (dir == "asc") {
          if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        }
      }
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        switchcount ++;
      } else {
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }

/*-------------------------------------------------*/
const resDiv = document.getElementById("content");
const resizer = document.querySelector("div.content--resizer");

const initResize = e => {
  e.preventDefault;
  window.addEventListener("mousemove", startResize);
  window.addEventListener("mouseup", stopResize);
};

const startResize = e => {
  resDiv.style.width = (e.clientX - resDiv.offsetLeft) + "px";
};
const stopResize = e => {
  window.removeEventListener('mousemove', startResize);
  window.removeEventListener('mouseup', stopResize);
};

resizer.addEventListener("mousedown", initResize);