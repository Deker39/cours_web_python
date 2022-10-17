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



$('#red').click(function(){
    $('[name=redFruit]').addClass('item-shadow')
    $('[name]:not([name=redFruit])').removeClass('item-shadow')
})
$('#green').click(function(){
    $('[name=greenFruit]').addClass('item-shadow')
    $('[name]:not([name=greenFruit])').removeClass('item-shadow')
})
$('#orange').click(function(){
    $('[name=orangeFruit]').addClass('item-shadow')
    $('[name]:not([name=orangeFruit])').removeClass('item-shadow')
})
$('#blue').click(function(){
    $('[name=blueFruit]').addClass('item-shadow')
    $('[name]:not([name=blueFruit])').removeClass('item-shadow')
})



