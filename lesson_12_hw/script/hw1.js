/*-----------------------------------------------*/

let p = document.getElementById('name')

p.addEventListener('keydowm',function(e){
    if( e.key.match(/[0-9]/) ) return e.preventDefault();
}) 

p.addEventListener('input', function(e){
  p.value = p.value.replace(/[0-9]/g, "");
});

/*-----------------------------------------------*/
let win = document.getElementById('myModal')

  function foo(){
    win.style.display = 'flex'
  }
  function f1(){
    win.style.display = 'none'
  }
/*-----------------------------------------------*/

function play() {
  window.open('footbal.html')
}

/*-----------------------------------------------*/
let color=['red','orange','green']
let n = document.getElementById('next')
let round = document.querySelectorAll('.cicle')
let i = -1
function next(){
  i++
  if(round[i-1]) round[i-1].style.backgroundColor = ''
  if(i == color.length) i = 0
  round[i].style.backgroundColor = color[i]
}

/*-----------------------------------------------*/
var list = document.querySelectorAll('.bookList li');

function setSelected() {
	document.querySelectorAll('.bookList li.selected').forEach(function (el) {
  	el.classList.remove('selected');
  });
  this.classList.add('selected');
}

list.forEach(function(li) {
	li.onclick = setSelected;
});

/*-----------------------------------------------*/