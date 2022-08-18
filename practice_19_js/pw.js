/*-------------------------------------------------*/
var textLogin = document.getElementById('textLogin')
var checkRemember = document.getElementById('checkRemember')

function authorization() {

    let mainForm = document.forms[0]
    let elemLogin = mainForm.elements.textLogin;
    let elemRemember = mainForm.elements.checkRemember;

    if (elemRemember.checked == true) {
        alert(`Your account has been saved: ${elemLogin.value}`)
    } else {
        alert(`Your account has not been saved: ${elemLogin.value}`)
    }

}
/*-------------------------------------------------*/
const inputEmail = document.getElementById('inputEmail') 
const inputPassword =  document.getElementById('inputPassword') 
const inputPasswordReapeat =  document.getElementById('inputPasswordReapeat') 

// pass: 26091998@Qwe
function signUpEmail(){
    inputPassword.value == inputPasswordReapeat.value? alert(`A confirmation email has been sent to ${inputEmail.value}`): false
}
/*-------------------------------------------------*/
const form = document.getElementById('third'),
     inputFirstName =  document.getElementById('inputFirstName'),
     inputLirstName = document.getElementById('inputLirstName'),
     inputBirthday = document.getElementById('inputBirthday'),
     radioGender = document.querySelectorAll('input[name="flexRadioDefault"]'),
     inputCountry = document.getElementById('inputCountry'),
     inputCity = document.getElementById('inputCity')

let title = ['First name','Last name','Birthday','Gender','Country','City','Skills'],
     arrayInfo = [],
     skill = [],
     gender 

form.onsubmit = function () {

    for (const radioButton  of radioGender){
        if(radioButton.checked){
            gender = radioButton.value
            break;
        }
    }

    document.querySelectorAll('input[name="skills"]:checked').forEach((e) => {
        skill.push(e.value)
    })

    arrayInfo.push(inputFirstName.value,inputLirstName.value,inputBirthday.value,
        gender,inputCountry.value,inputCity.value,skill.join(', '))

    localStorage.setItem(`table`, JSON.stringify(arrayInfo))
    
}

if (JSON.parse(localStorage.getItem('table'))){
    var getArrayTable = JSON.parse(localStorage.getItem('table'))

    let table = document.createElement('table')
    let tbody = document.createElement('tbody')

    table.classList.add('table', 'table-striped','table-primary')

    for (let i = 0; i < 7; i++) {
        let tr = document.createElement('tr')

        let th = document.createElement('th')
        let td = document.createElement('td')

        th.setAttribute('scope','row')

        th.innerHTML = title[i]
        td.innerHTML = getArrayTable[i]

        tr.appendChild(th)
        tr.appendChild(td)
        tbody.appendChild(tr);

        
    }

    table.appendChild(tbody)
    document.getElementById('thirdSection').appendChild(table)
}





/*-------------------------------------------------*/
const rgbForm = document.getElementById('fourth'),
    red = document.getElementById('red'),
    green = document.getElementById('green'),
    blue = document.getElementById('blue'),
    inputRGB = document.querySelectorAll('input[name="rgb"]')
let counter = 0,
    userColors = []


function creatRGBItem(colorRed,colorGreen,colorBlue){
    let contRGB = document.getElementById('contRGB')
    let divitem =  document.createElement('div')
    let divColor = document.createElement('div')
    let hName = document.createElement('h5')
    
    divitem.classList.add('border', 'd-flex', 'align-items-center', 'm-3')
    divColor.classList.add('cont')
    hName.classList.add('p-2', 'pe-4', 'ps-3','mb-0')

    divColor.style.backgroundColor = `RGB(${colorRed},${colorGreen},${colorBlue})`

    hName.textContent = `RGB( ${colorRed}, ${colorGreen}, ${colorBlue})`

    contRGB.appendChild(divitem)
    divitem.appendChild(divColor)
    divitem.appendChild(hName)
}

class ColorObject  {
    constructor(red,green,blue){
        this.red = red;
        this.green = green;
        this.blue = blue
    }
    toString(){
        return `${this.red};${this.green};${this.blue};`
        }
}

function getColorsfromCookie(){

    let cookieString = decodeURIComponent(document.cookie);
    let cookieArray = cookieString.split("; ")

    if(cookieArray.length < 0) return;
    else{
        for (let i = 0; i < cookieArray.length; i++) {

            if(/^color/.test(cookieArray[i])){
              let colorItem = cookieArray[i].split("=");
              let colorValues = colorItem[1].split(";");
              userColors.push(new ColorObject(colorValues[0], colorValues[1], colorValues[2]))
            }
            if(/^counter/.test(cookieArray[i])){
                let counterItem = cookieArray[i].split("=");
                let counterValue = +(counterItem[1]);
                counter += counterValue;
              }
          }
    }
}


getColorsfromCookie()
if(userColors.length > 0){
    userColors.forEach(item =>{
        creatRGBItem(item.red,item.green,item.blue)
    })
    
}

rgbForm.onsubmit = function(){

    inputRGB.forEach(function (input){
        if(input.value === '' || input.value === ' ' || input.value < 0 || input.value > 255){
            input.classList.add('is-invalid')
            return false
        }else{
            input.classList.remove('is-invalid')
            input.classList.add('is-valid')
        }  
    })

    if(!red.value ||  !green.value || !blue.value || !red.value && !green.value && !blue.value ){
            return false
        }
        else{
            if(red.value < 0 || red.value > 255 || green.value < 0 || green.value > 255 || blue.value < 0 || blue.value > 255){
                return false
            }else{
                creatRGBItem(red.value,green.value,blue.value)

                let newRGB = new ColorObject(red.value,green.value,blue.value)
                userColors.push(newRGB)

                let date = new Date(Date.now() + 86400e3);
                date = date.toUTCString();

                let colorkey = "color" + counter;
                counter++

                document.cookie = `${colorkey}=${encodeURIComponent(newRGB.toString())}; max-age=60; path=/`
                document.cookie = `counter=${counter}; path=/`;
                //пределать на обьект для отправки в куки 
                
            }
  
        }

    
    

    return false
}



/*-------------------------------------------------*/
