var colorReg = RegExp(/[a-zA-Z]/)
var rgbReg  = RegExp(/(\d{1,3}),(\d{1,3}),(\d{1,3})/)
var rgbareg = RegExp(/(\d{1,3}),(\d{1,3}),(\d{1,3}),(1|1\.?\.0|0\.?\.\d{0,}|0)/ )
var hexReg = RegExp(/#[0-9A-Fa-f]{6}/)


// var mainDiv = document.getElementById('view')
// var creatDiv = document.createElement('div')
// var colorName = document.getElementById('colorId')
// var colorType = document.getElementById('typeId')
// var colorCode = document.getElementById('codeId')
// console.log(colorName.textContent);

let form = document.querySelector('#form'),
    formInputs = document.querySelectorAll(".form-control"),
    inputColorName  = document.querySelector('#colorId'), 
    inputColorType  = document.querySelector('#typeId'), 
    inputColorCode  = document.querySelector('#codeId'),
    emptyInputs = Array.from(formInputs).filter(input => input.value === ''),
    colorError  = document.querySelector('#colorError'),
    codeError = document.querySelector('#codeError')

function validtateColorName(name){
    let reg = /[a-zA-Z]/
    return reg.test(name)
}

function validtateRGB(code){
    let reg = /(\d{1,3}),(\d{1,3}),(\d{1,3})/
    return reg.test(code)
}

function validtateRGBA(code){
    let reg = /(\d{1,3}),(\d{1,3}),(\d{1,3}),(1|1\.?\.0|0\.?\.\d{0,}|0)/
    return reg.test(code)
}

function validtateHEX(code){
    let reg = /#[0-9A-Fa-f]{6}/
    return reg.test(code)
}

form.onsubmit  = function(){
    let colorNameValue = inputColorName.value,
        colorColorType = inputColorType.value,
        colorColorCode = inputColorCode.value

    // console.log(colorNameValue,colorColorType,colorColorCode);

    formInputs.forEach(function (input){
        if(input.value === '' || input.value === ' '){
            input.classList.add('is-invalid')
        }else{
            input.classList.remove('is-invalid')
        }
        
    });

    

    if (!validtateColorName(colorNameValue)){
        inputColorName.classList.add('is-invalid')
        colorError.classList.remove('display-none')
        console.log('Name not valid')
        // return false
    }else{
        colorError.classList.add('display-none')
        inputColorName.classList.remove('is-invalid') 
        inputColorName.classList.add('is-valid') 
       
    } 


    if(colorColorType == 'rgb'){
        if(!validtateRGB(colorColorCode)){
            var p = document.createElement('p')
            codeError.appendChild(p)
            p.innerText ='RGB code must match the pattern [0-255],[0-255],[0-255]'
            p.classList.add('text-danger')
            
            codeError.classList.remove('display-none')
            inputColorCode.classList.add('is-invalid')
            console.log('Code RGB not valid')
            return false
        }else{
            codeError.classList.add('display-none')
            inputColorCode.classList.remove('is-invalid') 
            inputColorCode.classList.add('is-valid')
        }
    }

    if(colorColorType == 'rgba'){
        if(!validtateRGBA(colorColorCode)){
            var p = document.createElement('p')
            codeError.appendChild(p)
            p.innerText ='RGBA code must match the pattern [0-255],[0-255],[0-255],[0-1]'
            p.classList.add('text-danger')

            codeError.classList.remove('display-none')
            inputColorCode.classList.add('is-invalid')
            console.log('Code RGBA not valid')
            return false
        }else{
            codeError.classList.add('display-none')
            inputColorCode.classList.remove('is-invalid') 
            inputColorCode.classList.add('is-valid')
        }
    }
    // 'HEX code must match the hexadecimal pattern #[0-F],[0-F],[0-F],[0-F],[0-F],[0-F]'
    if(colorColorType == 'hex'){
        if(!validtateHEX(colorColorCode)){
            var p = document.createElement('p')
            codeError.appendChild(p)
            p.innerText ='HEX code must match the hexadecimal pattern #[0-F],[0-F],[0-F],[0-F],[0-F],[0-F]'
            p.classList.add('text-danger')

            codeError.classList.remove('display-none')
            inputColorCode.classList.add('is-invalid')
            console.log('Code HEX not valid')
            return false
        }else{
            codeError.classList.add('display-none')
            inputColorCode.classList.remove('is-invalid') 
            inputColorCode.classList.add('is-valid')
        }
    }

    

    if(emptyInputs.length !== 0){
        console.log('input not filled');
        // return false
    }

    return false
}