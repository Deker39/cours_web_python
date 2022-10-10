$('#road').mousemove(function(event){
    let roadCoords = this.getBoundingClientRect();

    let catCoords = {
        top: event.clientY - roadCoords.top - road.clientTop - rainboCat.clientHeight / 2,
        left: event.clientX - roadCoords.left - road.clientLeft - rainboCat.clientWidth / 2
      };

    rainboCat.style.left = catCoords.left + 'px';
    rainboCat.style.top = catCoords.top + 'px';
})

$('#menu').click(function(){

    $('.link').toggleClass('display-block')
    $('.cont-menu-setting').first().css('justify-content','center')

})


