
var textLogin = document.getElementById('textLogin')
var textPassword = document.getElementById('textPassword')
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

