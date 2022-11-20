let cardPicturesSet = ['circle.svg', 'heart.svg.webp', 'square.png', 'star.svg.png', 'triangle.svg.png', 'circle.svg', 'heart.svg.webp', 
                    'square.png', 'star.svg.png', 'triangle.svg.png'],
    count = 0,
    indexChoose = [],
    choose = []

const shuffle = (arr) => {
    return arr.sort(() => Math.round(Math.random() * 100) - 50);
}

shuffle(cardPicturesSet)

cardPicturesSet.slice(0,5).forEach(e => {
    $(`<div class="col border rounded bg-secondary bg-opacity-25 p-4 py-5 m-2"><img name="card" src="${e}" alt=""
    style="width: 90px; height: 90px;"></div>`).appendTo($('#sect1').children()[0])
});

cardPicturesSet.slice(5,10).forEach(e => {
    $(`<div class="col border rounded bg-secondary bg-opacity-25 p-4 py-5 m-2"><img name="card" src="${e}" alt=""
    style="width: 90px; height: 90px;"></div>`).appendTo($('#sect1').children()[1])
});

function creatCardPict(e){
    $(e).attr('src',cardPicturesSet[$("[name='card']").index(e)])
    $(e).css({'max-width': '', 'height': '90px', 'width':'90px'})
    $(e).parent().addClass('p-4 py-5')
    $(e).parent().removeClass('p-0')
    $(e).removeClass('opacity-50')
}

function creatCardShort(e){
    $(e).attr('src','shorts.png')
    $(e).css({'max-width': '100%', 'height': '188px', 'width':''})
    $(e).parent().addClass('p-0')
    $(e).parent().removeClass('p-4 py-5')
    $(e).removeClass('opacity-50')
}

$('#start').click(function(){
    if ($("#start").html() == "START"){
        $("#start").html('FINISH')

        $.each($("[name='card']"), function(index,value){
            creatCardShort(value)
        }) 
        
        $("[name='card']").on('click',function(){
            
            if( count < 2){   

                choose.push(cardPicturesSet[$("[name='card']").index(this)])
                indexChoose.length == 2? indexChoose = []: false
                indexChoose.push($("[name='card']").index(this))
                creatCardPict(this)

                count++

                if(choose.length == 2){
                    if(choose[0] == choose[1]){
                        console.log('verno');     
                        $("[src='shorts.png']").length == 0? alert('You win'): false      
                        $($("[name='card']")[indexChoose[0]]).addClass('opacity-50')    
                        $($("[name='card']")[indexChoose[1]]).addClass('opacity-50')         
                    }
                    else{
                        console.log('neverno');
                        setTimeout(() => [creatCardShort($("[name='card']")[indexChoose[0]]),creatCardShort($("[name='card']")[indexChoose[1]])], 1000);
                    }                
                    count = 0
                    choose = []
 
                } 
                
                     
            }  
           
        })
      
    }
    else{
        $("#start").html('START')
        $.each($("[name='card']"), function(index,value){
            creatCardPict(value)
        })    
    } 

 
})



