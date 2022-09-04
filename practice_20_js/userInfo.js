const secondForm = document.getElementById('secondForm'),
    linkExit = document.getElementById('exit'),
    inputFirstName = document.getElementById('inputFirstName'),
    inputLastName = document.getElementById('inputLastName'),
    inputBirthday = document.getElementById('inputBirthday'),
    selectGender = document.getElementById('selectGender'),
    inputPhoneNumber = document.getElementById('inputPhoneNumber'),
    inputSkype = document.getElementById('inputSkype'),
    greetings = document.getElementById('greetings')

let arrayUser = new Array(),
    us

class UserInfoMore{
    constructor(firstName,lastName,birthday,gender,phoneNumber,skype){
        this.login = arrayUser.find(e => e.includes(us)).split('=')[1].split(';')[0];
        this.pass = arrayUser.find(e => e.includes(us)).split('=')[1].split(';')[1];
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

function getCookie(){
    let cookieString = decodeURIComponent(document.cookie);
    let cookieArray = cookieString.split("; ")
    console.log(cookieArray);
    return cookieArray
}

function getUsersfromCookie(){

    let cookieArray = getCookie()

    arrayUser = cookieArray

    if(cookieArray.length < 0) return;
    else {
        for (let i = 0; i < cookieArray.length; i++) {

            // if (/^user/.test(cookieArray[i])) {
            //     let userItem = cookieArray[i].split("=");
            //     userValues = userItem[1].split(";").slice(0, 2)
            //     // console.log(userValues);
               

            // }

            if (/^loggedIn/.test(cookieArray[i])) {
                us = cookieArray[i].split("=")[1]
            }
            
            
        }
    }
  }

// прописать даныне того кто зашел проверка поп почте 
// inputFirstName.value = '123'
// inputLastName.value = '123'
// inputBirthday.value = '123'
// selectGender.value = 'male'
// inputPhoneNumber.value = '123'
// inputSkype.value = '123'
getUsersfromCookie()


greetings.classList.remove('display-none')
greetings.prepend(`Hello,  ${arrayUser.find(e => e.includes(us)).split('=')[1].split(';')[0]} `)


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
        console.log(us);
    let kek =  new UserInfoMore(inputFirstName.value, inputLastName.value, inputBirthday.value, selectGender.value,
        inputPhoneNumber.value, inputSkype.value)
        console.log(kek);
        document.cookie = `${us}=${encodeURIComponent(new UserInfoMore(inputFirstName.value, inputLastName.value, inputBirthday.value, selectGender.value,
            inputPhoneNumber.value, inputSkype.value).toString())};max-age=3600; path=/`

    return false


}