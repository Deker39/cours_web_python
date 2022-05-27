/*-----------------------------------------------*/

let p = document.getElementById('name')

p.addEventListener('keydowm',function(e){
    if( e.key.match(/[0-9]/) ) return e.preventDefault();
}) 

p.addEventListener('input', function(e){
  p.value = p.value.replace(/[0-9]/g, "");
});

/*-----------------------------------------------*/
let b = document.getElementById('open')
let c = document.getElementById('close')
let win = document.getElementById('myModal')

  function foo(){
    document.addEventListener('click', function(e) {
      if (b){
        win.style.display = 'flex'
      }else{
        win.style.display = 'none'
      }
  
    })
  }
  function f1(){
    document.addEventListener('click', function(e) {
    if(c){
      win.style.display = 'none'
    }else {
      win.style.display = 'flex'
    }
    })
  }
/*-----------------------------------------------*/
let k = document.getElementById('play')

function play(){document.addEventListener('click', (e) =>  window.open('footbal.html'))}

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
