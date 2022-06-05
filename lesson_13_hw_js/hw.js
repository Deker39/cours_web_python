/*-------------------------------------------------*/

var ul = document.querySelectorAll('#first .list-group a:is([href^="https://"])')
ul.forEach(function(el){
    el.style.color = 'green'
    el.style.borderBottom = "2px dashed green"
})

/*-------------------------------------------------*/
var first_list = document.getElementById('first_list')
// var second_list  = document.getElementById('second_list')
// var third_list = document.getElementById('third_list')

var first_list_arr = document.querySelectorAll('#first_list > li')
// var second_list_arr = document.querySelectorAll('#second_list > li')
// var third_list_arr = document.querySelectorAll('#third_list > li')

// var lel  = document.querySelectorAll('#first_list > *')

// console.log(document.querySelectorAll('li'));

first_list.onclick = function(){
    // second_list.classList.add('display-block')
    first_list.childNodes.item(1).childNodes.item(1).classList.add('display-block')
    console.log(first_list.childNodes.item(1).childNodes.item(1));
    set
    
}
    


function set(){
    document.querySelectorAll('#second_list > li.bold').forEach(function (el) {
        el.classList.remove('bold');
    });
    this.classList.add('bold')
}
// function cl(){
//     third_list.classList.add('display-block')
// }


// second_list.onclick = function(){
//     // third_list.classList.add('display-block')
//     this.childNodes.classList.add('display-block')
// }

// first_list.onclick = function(){
//     console.log(this.childNodes);
    // this.childNodes
    // second_list.classList.add('display-block')
    // second_list.classList.remove('display-block')
// }

// second_list_arr.forEach(function(li){
//     li.onmouseover = set
//     li.onclick = function(){
//         console.log(li.children);
       
//         // li.childElementCount.target.classList.add('display-block')
//         // third_list.classList.add('display-block')

//     }
        
    
// })






