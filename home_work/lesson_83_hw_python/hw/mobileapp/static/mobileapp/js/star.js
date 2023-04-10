$('#startReating').on('click',function(event){

  if($('[style*="background-image:url(/static/mobileapp/images/star_black_32px.png)"]').length !== 5){
    $('#startReating').children().css('backgroundImage','url(/static/mobileapp/images/star_black_32px.png)')
  }

  for (let i = 0; i <= [].indexOf.call(this.children, event.target); i++) {
    $($('#startReating').children()[i]).css('backgroundImage','url(/static/mobileapp/images/star_ligth_32px.png)')
        }

})