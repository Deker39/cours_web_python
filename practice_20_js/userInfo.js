const secondForm = document.getElementById('secondForm'),
    linkExit = document.getElementById('exit'),
    inputFirstName = document.getElementById('inputFirstName'),
    inputLastName = document.getElementById('inputLastName'),
    inputBirthday = document.getElementById('inputBirthday'),
    selectGender = document.getElementById('selectGender'),
    inputPhoneNumber = document.getElementById('inputPhoneNumber'),
    inputSkype = document.getElementById('inputSkype'),
    greetings = document.getElementById('greetings')

// прописать даныне того кто зашел проверка поп почте 
inputFirstName.value = '123'
inputLastName.value = '123'
inputBirthday.value = '123'
selectGender.value = 'male'
inputPhoneNumber.value = '123'
inputSkype.value = '123'

greetings.classList.remove('display-none')
greetings.prepend('Hello, Jhon,smith@gmail.com! ')

linkExit.onclick() = function(){
    // удаление куки с браузера
}

secondForm.onsubmit = function(){
    // ввести данные пользователя и сохранть их в куки 

    return false


}