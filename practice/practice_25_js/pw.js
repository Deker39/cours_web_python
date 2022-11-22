let count = 0,
    index,
    indexBack,
    nestingDepthJSON = ['regions','schools','classes']

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
    $(`<div name="${nestingDepthJSON[count]}" class="d-flex flex-column border border-dark m-3" style="width: 300px; height:100%">
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

function recursiveHandler(data){
    $(`[name='${nestingDepthJSON[count]}']`).on('click',function(){
        index = $(`[name='${nestingDepthJSON[count]}']`).index($(this))

        $(`[name='regions']`).length != 0?  indexBack = $(`[name='regions']`).index($(this)): false

        count ++

        $("[type='button']").hasClass('display-block')? false: $("[type='button']").addClass('display-block')

        // условие на глубину

        if(count == 1){
            $('#contCards').empty()
            data['regions'][index][nestingDepthJSON[count]].forEach(e => {
                creatCard(e['schoolName'],e['filledPlaces'],e['allPlaces'])
            })
            $('#title').append(`-> ${data['regions'][index]['regionName']}`)

            recursiveHandler(data)
        }
        else if(count == 2){
            $('#contCards').empty()
            data['regions'][indexBack][nestingDepthJSON[count-1]][index][nestingDepthJSON[count]].forEach(e => {
                creatCard(e['className'],e['filledPlaces'],e['allPlaces'])
            });  
            $('#title').append(`-> ${data['regions'][indexBack][nestingDepthJSON[count-1]][index]['schoolName']}`)
        }   
    })
}

function creatPaletteCards(data){

    $(` <h5 class="text-center" id="title">CITY: ${data['cityName'] }</h5>
    <div id="contCards" class="d-flex flex-wrap justify-content-center">
    </div>`).appendTo('#sectCard')

    data[nestingDepthJSON[count]].forEach(e => {
        creatCard(e['regionName'],e['filledPlaces'],e['allPlaces'])
    })

    recursiveHandler(data)

    $("[type='button']").on('click',function(){
        count --
        $('#contCards').empty()
        
        if (count == 0){
            data[nestingDepthJSON[count]].forEach(e => {
                creatCard(e['regionName'],e['filledPlaces'],e['allPlaces'])
            })

            var text = $('#title').html();
            text = text.replace(`-&gt; ${data['regions'][indexBack]['regionName']}`, '');
            $('#title').html(text);

            recursiveHandler(data)
        }
        else if(count == 1){      
            data['regions'][indexBack][nestingDepthJSON[count]].forEach(e => {
                creatCard(e['schoolName'],e['filledPlaces'],e['allPlaces'])
            })

            var text = $('#title').html();
            text = text.replace(`-&gt; ${data['regions'][indexBack][nestingDepthJSON[count]][index]['schoolName']}`, '');
            $('#title').html(text);

            recursiveHandler(data)
        }

        count == 0?$("[type='button']").removeClass('display-block'): false
        
    })
}

$.getJSON('citySchoolOccupancyStudents.json',function(data){
    console.log(data);
    creatPaletteCards(data)
})

