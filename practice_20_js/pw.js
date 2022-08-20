const firsrForm = document.getElementById('first'),
    textLogin = document.getElementById('textLogin'),
    textPassword = document.getElementById('textPassword'),
    textRepeatPassword = document.getElementById('textRepeatPassword'),
    allInput = document.querySelectorAll('input[name="enter"]')



firsrForm.onsubmit = function(){

    allInput.forEach(function (input){
        if(input.value === '' || input.value === ' '){
            input.classList.add('is-invalid')
            return false
        }else{
            input.classList.remove('is-invalid')
            input.classList.add('is-valid')
        }  
    })

    if(textPassword.value == textRepeatPassword.value && textPassword.value != '' && textRepeatPassword.value != ''){
        console.log(textLogin.value,textPassword.value,textRepeatPassword.value);
    }else{
        return false
    }

    return false




}

    
    
