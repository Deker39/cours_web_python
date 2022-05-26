let p = document.getElementById('name')

p.addEventListener('keydowm',function(e){
    if( e.key.match(/[0-9]/) ) return e.preventDefault();
}) 

p.addEventListener('input', function(e){
  p.value = p.value.replace(/[0-9]/g, "");
});

