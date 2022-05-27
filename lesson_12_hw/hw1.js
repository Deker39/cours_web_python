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

function play(){
  document.addEventListener('click', function(e) {
    if(k){
      window.open('footbal.html')
    }
})
}
/*-----------------------------------------------*/