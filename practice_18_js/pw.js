/*-------------------------------------------------*/
const numb = document.getElementById('numb')

numb.addEventListener('keydown', e => e.preventDefault())

/*-------------------------------------------------*/

const addColor = document.getElementById('btnAddColor')
const contBlock = document.getElementById('contBlock')

addColor.onclick = function(){
    const divColor = document.createElement('div')
    divColor.classList.add('box')
    divColor.style.backgroundColor = `#${(Math.random().toString(16) + '000000').substring(2,8).toUpperCase()}`

    contBlock.appendChild(divColor)
}
contBlock.addEventListener('click', event =>{ event.target == event.currentTarget? false: event.target.remove() })
/*-------------------------------------------------*/

const palitra = document.getElementById('palitra')


for(var i = 0; i < 20; i++){
     const divBlockPalit  = document.createElement('div')
     divBlockPalit.classList.add('s-box')
     divBlockPalit.classList.add('col')
     divBlockPalit.classList.add('border')
     divBlockPalit.style.backgroundColor = `#${(Math.random().toString(16) + '000000').substring(2,8).toUpperCase()}`
     palitra.appendChild(divBlockPalit)
}


// document.querySelectorAll('#palitra div')
palitra.addEventListener('click', event =>{
    event.target == event.currentTarget? false:  document.getElementById('text').style.color = event.target.style.backgroundColor
   
})

/*-------------------------------------------------*/
/*-------------------------------------------------*/