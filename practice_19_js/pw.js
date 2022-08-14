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

/*-------------------------------------------------*/
/*-------------------------------------------------*/
