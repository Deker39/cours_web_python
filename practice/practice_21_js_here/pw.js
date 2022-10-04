class User {
    constructor(id, name, username, phone, email, company, address, website) {
      (this.id = id),
        (this.name = name),
        (this.username = username),
        (this.phone = phone),
        (this.email = email),
        (this.company = company),
        (this.address = address),
        (this.website = website);
    }
  }
  
  var listUsers = Array();


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




async function loadFetch() {
    const res = await fetch("https://jsonplaceholder.typicode.com/users");
    const body = await res.json();
    if (body) {
        listUsers = body.map(
        (i) =>
          new User(
            i.id,
            i.name,
            i.username,
            i.phone,
            i.email,
            i.company,
            i.address,
            i.website
          )
      );

      listUsers.forEach((e) => {
        $("#contCard").append(
          $(`<div class="border col-3 p-3 pe-4 m-3" id="user${e.id}"><h5>${e.name}</h5></div>`)
        );
      });
    }
  }

loadFetch()

$("#contCard").on('click','div', function(){
    console.log(($( this ).attr('id')).replace('user',''));
    let selectedUser = ($( this ).attr('id')).replace('user','')-1
    console.log(listUsers[selectedUser].name);
    $('body').append(
        $(`
        <section class="container d-flex align-items-center justify-content-center  flex-column">
            <h5>All users:</h5>
            <table class="table table-responsive table-bordered ">
                <tbody>
                    <tr>
                    <th scope="row" class=" ">Name:</th>
                    <td class="ps-4">${listUsers[selectedUser].name}</td>
                    </tr>
                    <tr>
                    <th scope="row" class=" ">Username:</th>
                    <td class="ps-4">${listUsers[selectedUser].username}</td>
                    </tr>
                    <tr>
                    <th scope="row" class=" ">Address:</th>
                    <td class="ps-4">${listUsers[selectedUser].address}</td>
                    </tr>
                    <tr>
                    <th scope="row" class=" ">Email:</th>
                    <td class="ps-4">${listUsers[selectedUser].email}</td>
                    </tr>
                    <tr>
                    <th scope="row" class=" ">Phone:</th>
                    <td class="ps-4">${listUsers[selectedUser].phone}</td>
                    </tr>
                    <tr>
                    <th scope="row" class=" ">Website:</th>
                    <td class="ps-4">${listUsers[selectedUser].website}</td>
                    </tr>
                </tbody>
                </table>
                
        </section>`
        )
    )
})





