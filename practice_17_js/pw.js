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
/*-------------------------------------------------*/
/*-------------------------------------------------*/