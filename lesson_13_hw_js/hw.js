/*-------------------------------------------------*/

var ul = document.querySelectorAll('#first .list-group a:is([href^="https://"])')
ul.forEach(function(el){
    el.style.color = 'green'
    el.style.borderBottom = "2px dashed green"
})

/*-------------------------------------------------*/
 var li =  document.querySelectorAll('#second .list-group .list-group-item')
 var li_ul =  document.querySelectorAll('#second .list-group ul')
 
function setSelected(){
    li.forEach(function (el) {
        el.style.fontWeight = "bold";
        li_ul.forEach(function(el){
            el.style.display = 'block'
        })
    });
 }

//обращаеться ко всем а не к одному
li.forEach(function(el){
    el.onclick  = setSelected
})

 console.log(li);

