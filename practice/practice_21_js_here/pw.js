
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
async function Test(){
    const res = await fetch('https://jsonplaceholder.typicode.com/users')
    return res
}
let user = new Array()


//   .then(response => response.json())
//   .then(item => item.forEach(i => {user.push(i)}))

Test().then(response => response.json())
    .then(item => item.forEach(i => {user.push(i)}))


console.log(user)

// console.log()

// for (let i = 0; i < user.length; i++) {
//     console.log(user[i]['name']);
    
// }

user.forEach(e => {
    console.log(e);
});


$('#contCard').append($(`<div class="border p-3 pe-4 m-3"><h4>'kek'</h4></div>`))





