$(function(){ $('.circle').circle(); });

function checkColor(filledPlaces,allPlaces){
    res = Math.round((filledPlaces / allPlaces)*10)
    if (0 < res && res <= 2){
        return 'darkseagreen'
    }
    else if((2 < res && res <= 4)){
        return 'darkcyan'
    }else if((4 < res && res <= 6)){
        return 'darksalmon'
    }
    else if((6 < res && res <= 8)){
        return 'darkorange'
    }else{
        return 'darkred'
    }

}

function creatCard(name,filledPlaces,allPlaces){
    $(`<div name="card" class="d-flex flex-column border border-dark m-3" style="width: 300px; height:100%">
            <p class="text-center m-1">${name}</p>
            <hr class="m-0 opacity-100">
            <div class="circle" data-circleconfig='{"color": "${checkColor(filledPlaces,allPlaces)}",
             "graduation": 10, "fill": ${Math.round((filledPlaces/allPlaces)*10)}}' ></div>
            <hr class="m-0 opacity-100">
            <div class="d-flex flex-row justify-content-evenly">
                <div class="d-flex flex-column justify-content-center align-items-center">
                    <p class="text-center text-nowrap m-0">places filled</p>
                    <p>${filledPlaces}</p>
                </div>
                <hr class="border opacity-100 m-1">
                <div class="d-flex flex-column justify-content-center align-items-center">
                    <p class="text-center text-nowrap m-0">out of places availible</p>
                    <p>${allPlaces}</p>
                </div>
        </div> `).appendTo('#contCards')
        $(function(){ $('.circle').circle(); });
}

function creatPaletteCards(data){

    $(` <h5 class="text-center">CITY: ${data['cityName']}</h5>
    <div id="contCards" class="d-flex flex-wrap justify-content-center">
    </div>`).appendTo('#sectCard')

    data['regions'].forEach(e => {
        creatCard(e['regionName'],e['filledPlaces'],e['allPlaces'])
    })

    // может нажо будет изменить место 
    $("[name='card']").on('click',function(){
        index = $("[name='card']").index($(this))
        $('#contCards').empty()
        console.log(data['regions'][index]['schools'])

        
        data['regions'][index]['schools'].forEach(e => {
            creatCard(e['schoolName'],e['filledPlaces'],e['allPlaces'])
            
        });

    })
}


$.getJSON('citySchoolOccupancyStudents.json',function(data){
    console.log(data);
    creatPaletteCards(data)
})

