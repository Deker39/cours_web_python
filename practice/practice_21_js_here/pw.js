
$('#btn').click(function(){
    $('#floatingTextarea2').text(JSON.stringify((JSON.parse($('#floatingTextarea1').val())), 'null', 4))
}) 