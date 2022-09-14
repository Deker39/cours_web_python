/*-------------------------------------------------*/
const tb = document.getElementById('table')

tb.addEventListener('mouseover', (event) =>{
    event.target.style.backgroundColor  = '#ffa366'
}, false);
tb.addEventListener('mouseout', (event) =>{
    event.target.style.backgroundColor  = 'white'
}, false);
/*-------------------------------------------------*/
const cont = document.getElementById('content')

cont.addEventListener('contextmenu', event => event.preventDefault());
cont.onselectstart = (e) => {return false}
cont.onmousedown = (e) => {return false}

/*-------------------------------------------------*/
const like = document.getElementById('like')
var i = 0
like.onclick = function(){
    document.querySelector('#like > span').textContent  = `Like ${i++}`

}
/*-------------------------------------------------*/
const equal = document.querySelector('.btn-equal')
const numbers = document.querySelectorAll('.btn-number')
const sing = document.querySelectorAll('.btn-sing')
const vvod = document.querySelector('.vvod')

let result = new String()

numbers.forEach( e =>{
    e.onclick = function(){
        console.log(e.textContent);
        result += e.textContent
        vvod.textContent == '0'?  vvod.innerHTML =  e.textContent: vvod.textContent += e.textContent
    }
})
sing.forEach( e =>{
    e.onclick = function(){
        console.log(e.textContent);
        result += e.textContent
        vvod.textContent == '0'?  vvod.innerHTML =  e.textContent: vvod.textContent += e.textContent
    }
})

equal.onclick = function(){
   console.log(eval(result));
   vvod.textContent = eval(result)
   setTimeout(() =>  vvod.innerHTML = '0', 2000);
}
/*-------------------------------------------------*/
const list = document.getElementById('list')

list.addEventListener('mouseover',function(e) {
    e.target.children[0].classList.toggle('display-block')
})

/*-------------------------------------------------*/

const scroll = document.querySelector('.scrollup')


scroll.onclick = function(){
    window.scrollTo(0, 0) 
}

window.addEventListener('scroll', function() {
    pageYOffset > 100? scroll.style.display = 'block':scroll.style.display = 'none'

})
