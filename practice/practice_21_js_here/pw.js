
$('#btn').click(function(){
    // {"name":"John", "age":30, "car":null}
    try{
        $('#floatingTextarea2').text(JSON.stringify((JSON.parse($('#floatingTextarea1').val())), 'null', 4))
        $('#floatingTextarea1').addClass('is-valid')
        $('#floatingTextarea1').removeClass('is-invalid')
    }
    catch (e){
        $('#floatingTextarea1').addClass('is-invalid')
        $('#floatingTextarea1').removeClass('is-valid')
        $('#floatingTextarea2').text = ''
    }
   
}) 

let user = new Array()

fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then(item => item.forEach(i => {console.log(i['name'])}))




// console.log(user)

// for (let i = 0; i < user.length; i++) {
    // console.log(user[i]['name']);
    // 
// }

// user.forEach(e => {
//     console.log(e['name']);
// });


$('#contCard').append($(`<div class="border p-3 pe-4 m-3"><h4>'kek'</h4></div>`))





