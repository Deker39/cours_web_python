
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
async function loadFetch(){
    const res = await fetch('https://jsonplaceholder.typicode.com/users')
    return res
}
let listUser = new Array()

class User{
    constructor(id,name,username,phone,email,company,address,website){
        this.id = id,
        this.name = name,
        this.username = username,
        this.phone = phone,
        this.email = email,
        this.company = company,
        this.address = address,
        this.website = website
    }
}

function User1(id,name,username,phone,email,company,address,website){
    this.id = id,
    this.name = name,
    this.username = username,
    this.phone = phone,
    this.email = email,
    this.company = company,
    this.address = address,
    this.website = website
}


loadFetch().then(response => response.json())
    // .then(item => item.forEach(i => {listUser.push(new User(i.id,i.name,i.username,i.phone,i.email,i.company,i.address,i.website))}))
    .then(item => item.forEach(i => {listUser.push(new User(i.id,i.name,i.username,i.phone,i.email,i.company,i.address,i.website))}))


console.log(listUser)

listUser.forEach(e => {
    $('#contCard').append($(`<div class="border p-3 pe-4 m-3"><h4>${e.name}</h4></div>`))
});











