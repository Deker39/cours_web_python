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
const form = document.querySelector('#form'),
     formInputs = document.querySelectorAll(".form-control"),
     contComent = document.getElementById('contComent'),
     inputName = document.getElementById('textName'),
     inputComment = document.getElementById('textComment')

let array = []

function writeComment(name, time, comment){

    const div = document.createElement('div')
    const pName = document.createElement('h5')
    const pDate = document.createElement('p')
    const pComment = document.createElement('p')

    div.classList.add('shadow','p-3','mb-3','bg-info','bg-gradient','bg-opacity-25','rounded')

    pName.innerHTML = name
    pDate.innerHTML = time
    pComment.innerHTML = comment

    // array.forEach(e => {
    //     // pName.innerHTML = e.name
    //     // pDate.innerHTML = e.time
    //     // pComment.innerHTML = e.comment
    // });

    contComent.appendChild(div)
    div.appendChild(pName)
    div.appendChild(pDate)
    div.appendChild(pComment)

}


function Сoment(name, time, comment) {
    this.name = name;
    this.time = time;
    this.comment = comment;
}

form.onsubmit = function(){
       

    formInputs.forEach(function (input){
        if(input.value === '' || input.value === ' '){
            input.classList.add('is-invalid')
            return false
        }else{
            input.classList.remove('is-invalid')
            if (!inputName.value && !inputComment.value || !inputName.value && inputComment.value || inputName.value && !inputComment.value){
                return false 
            }else {
                // array.push(new Coment(inputName.value,new Date().toLocaleDateString(),inputComment.value))
                writeComment(inputName.value,new Date().toLocaleDateString(),inputComment.value)
                // pName.innerHTML = inputName.value
                // pDate.innerHTML = new Date().toLocaleDateString()
                // pComment.innerHTML = inputComment.value
                
            
                // contComent.appendChild(div)
                // div.appendChild(pName)
                // div.appendChild(pDate)
                // div.appendChild(pComment)
                
                
            }

        }
        
    });  

}


/*-------------------------------------------------*/