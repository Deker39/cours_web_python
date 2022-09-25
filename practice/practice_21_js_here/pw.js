
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
  .then(data => user.push(data))

  console.log(user);

