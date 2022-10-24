// Exercise#1
$('#road').mousemove(function(event){
    let roadCoords = this.getBoundingClientRect();

    let catCoords = {
        top: event.clientY - roadCoords.top - road.clientTop - rainboCat.clientHeight / 2,
        left: event.clientX - roadCoords.left - road.clientLeft - rainboCat.clientWidth / 2
      };

    rainboCat.style.left = catCoords.left + 'px';
    rainboCat.style.top = catCoords.top + 'px';
})
// Exercise#2
$('#menu').click(function(){

    $('.link').toggleClass('display-block')
    $('.cont-menu-setting').first().css('justify-content','center')

})
// Exercise#3
var fruit = ['red','green','orange','blue']

$('#listFruit').css('margin-top',`${$('#road').height()+50}px`)

fruit.forEach(e => $(`#${e}`).click(function(){
    $(`[name=${e}Fruit]`).addClass('item-shadow')
    $(`[name]:not([name=${e}Fruit])`).removeClass('item-shadow')
}))




// Exercise#4
$('#startReating').on('click',function(event){

  if($('[style*="background-image:url(/image/star_black_32px.png)"]').length != 5){
    $('#startReating').children().css('backgroundImage','url(/image/star_black_32px.png)')
  }

  for (let i = 0; i <= [].indexOf.call(this.children, event.target); i++) {
    $($('#startReating').children()[i]).css('backgroundImage','url(/image/star_ligth_32px.png)')
        }
 
})


