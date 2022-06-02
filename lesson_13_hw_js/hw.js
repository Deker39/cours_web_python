/*-------------------------------------------------*/

var ul = document.querySelectorAll('#first .list-group a:is([href^="https://"])')
ul.forEach(function(el){
    el.style.color = 'green'
    el.style.borderBottom = "2px dashed green"
})

/*-------------------------------------------------*/
var first_list = document.getElementById('first_list')
var second_list  = document.getElementById('second_list')
var third_list = document.querySelectorAll('#third_list')

 console.log(third_list);
first_list.onclick = function(){
    // second_list.classList.toggle('display-none')
    second_list.classList.add('display-block')
}

second_list.onclick = function(){
//     // second_list.classList.toggle('display-none')
    // third_list.classList.add('display-block')
    third_list.forEach(function(el) {
        el.classList.add('display-block')
    })

}



function setBold(){
    this.classList.add('bold');
}
function outBold(){
    this.classList.remove('bold');
}

// function setOpen(){
//     document.querySelectorAll('#second .list-group ul.open').forEach(function (el) {
//         el.classList.remove('open');
//     });
//     document.querySelectorAll('#second .list-group ul').forEach(function (el) {
//         console.log(el);
//         el.classList.add('open');
//     });

    
// }
    // this.style.fontWeight = "bold";
    // li.forEach(function (el) {
        // el.style.fontWeight = "bold";
        // li_ul.forEach(function(el){
            // this.classList.add('open')
        // })
    // });
 

// li.forEach(function(el){
//     el.onmouseover  = setBold
//     el.onmouseout = outBold
//     // el.onclick  = li_ul.setOpen
// })



