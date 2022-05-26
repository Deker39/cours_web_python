/*-----------------------------------------------*/

let p = document.getElementById('name')

p.addEventListener('keydowm',function(e){
    if( e.key.match(/[0-9]/) ) return e.preventDefault();
}) 

p.addEventListener('input', function(e){
  p.value = p.value.replace(/[0-9]/g, "");
});

/*-----------------------------------------------*/

  function foo(){
    let b = document.getElementById('open')
    let c = document.getElementById('close')
    let win = document.getElementById('myModal')
    document.addEventListener('click', function(e) {
      if (b){
        window.open('modal_win.html')
            
      }
      if(c){
        window.open('hw1.html')
      }
  
    })
  }
 

