const secondForm = document.getElementById('secondForm'),
    linkExit = document.getElementById('exit'),
    inputFirstName = document.getElementById('inputFirstName'),
    inputLastName = document.getElementById('inputLastName'),
    inputBirthday = document.getElementById('inputBirthday'),
    selectGender = document.getElementById('selectGender'),
    inputPhoneNumber = document.getElementById('inputPhoneNumber'),
    inputSkype = document.getElementById('inputSkype'),
    greetings = document.getElementById('greetings')

// import UserInfo from 'C:\Users\bigti\Desktop\cours_web_python\practice_20_js\registration.js'; 

class UserInfoMore extends UserInfo{
    constructor(login,pass,firstName,lastName,birthday,gender,phoneNumber,skype){
        super(login,pass)
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthday = birthday;
        this.gender = gender;
        this.phoneNumber = phoneNumber;
        this.skype = skype;
    }
    toString(){
        return `${this.login};${this.pass};${this.firstName};${this.lastName};${this.birthday};${this.gender};${this.phoneNumber};${this.skype};`
        }
    
}

// прописать даныне того кто зашел проверка поп почте 
// inputFirstName.value = '123'
// inputLastName.value = '123'
// inputBirthday.value = '123'
// selectGender.value = 'male'
// inputPhoneNumber.value = '123'
// inputSkype.value = '123'

greetings.classList.remove('display-none')
greetings.prepend('Hello, Jhon,smith@gmail.com! ')


// linkExit.onclick() = function(){
//     console.log('kek');
//     // удаление куки с браузера
// }

// function deleteCookie(name) {
//     setCookie(name, "", {
//       'max-age': -1
//     })
//   }

secondForm.onsubmit = function(){
    // ввести данные пользователя и сохранть их в куки 
    console.log(inputFirstName.value, inputLastName.value, inputBirthday.value, selectGender.value,
        inputPhoneNumber.value, inputSkype.value);

    return false


}