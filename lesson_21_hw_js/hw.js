
$.ajax({
    url: 'http://api.weatherstack.com/current',
    data: {
        access_key: 'ac722eb63a8bae3c2549219872c50e7d1',//1e2a81e7860ac4c2d569cfeaadf819c6
        //f9ed22455fb5f06608f849e0f82f7bd0
        query: 'Odesa'
    },
    dataType: 'json'
    }).done(function (data) {
    console.log(data);
    // $('body').parent().append( $(`<div class="container">${data.current.observation_time}</div>`))
    var secOneDayWeather = $('<section>',{
        'class':'container mb-3 mt-3',
        'style':'width: 500px;'  
    })
    var divOneDayWeather = $('<div>',{
        'class':'border rounded  d-flex justify-content-between grad-out'
    })
    var divContCityWeater = $('<div>',{
        'class':'d-flex justify-content-between flex-column p-3 '
    })
    var pNameCity = $('<p>',{
        'class':'fw-bold fs-1 border rounded p-2 grad-in',
        text:` ${data.location.name}, ${data.location.country}`
    })
    var divContIconTemperature = $('<div>',{
        'class':'d-flex justify-content-between border rounded p-2 grad-in'
    })
    var divContIconWeater = $('<div>')
    var divContIcon = $('<div>',{
        'class': 'border rounded',
        'style': `width:64px; height:64px;  background: url(${data.current.weather_icons})`
    })
    var pWeather = $('<p>',{
        'class':'text-center',
        'style':'width: 64px;',
        text: `${data.current.weather_descriptions}`
        
    })
    var temperature =  $('<p>',{
        'class':'fs-10',
        text: `${data.current.temperature}C°`
    })
    var divContTimeAddWeather = $('<div>',{
        'class':'m-3 border rounded p-2 grad-in ms-0'
        })
    var pTime = $('<p>',{
        class: 'fs-1 mb-4',
        text:`${data.location.localtime}`
    })
    var pWind = $('<p>',{
        text:`Wind: ${data.current.wind_speed}kph`
    })
    var pPrecip = $('<p>',{
        text:`Precip: ${data.current.precip}mm`
    })
    var pPressure = $('<p>',{
        text:`Pressure: ${data.current.pressure}mb`
    })


   $('body').append(secOneDayWeather
                .append(divOneDayWeather
                    .append(divContCityWeater
                        .append(pNameCity,divContIconTemperature
                                            .append(divContIconWeater
                                                .append(divContIcon,pWeather),temperature)),
                        divContTimeAddWeather
                            .append(pTime,pWind,pPrecip,pPressure))))

            })


// lat: "46.467"
// lon: "30.733"

$.ajax({
    url: 'https://api.openweathermap.org/data/2.5/forecast?',
    data: {
        lat: 46.467,
        lon: 30.733,
        appid: 'bf7329866498355636bce98b67774b95',
    },
    dataType: 'json'
}).done(function (data){
    console.log(data);

    var secFiveDayWeather = $('<section>',{
        'class':'container  mb-3 mt-4', 
    })
    var divFiveDayWeather = $('<div>',{
        'class':'d-flex justify-content-center align-items-center', 
    })
    var contDaysWeather = $('<div>',{
        'class':'d-flex flex-column align-items-center border -start grad-in p-3 ', 
    })
    var pDay =  $('<p>',{
        text:` ${Math.floor(data.list[0].main.temp-273.15)}C°`
    })
    var pDate =  $('<p>',{
        text:`${data.list[0].dt_txt}`
    })
    var divContIcon = $('<div>',{
        'class': 'border rounded',
        'style': `width:64px; height:64px;  background: url( http://openweathermap.org/img/wn/${data.list[0].weather[0].icon}.png) no-repeat; background-color: white;`
    })
    var pTemp = $('<p>',{
        text:`${data.list[0].weather[0].description}`
    })

    $('body').append(secFiveDayWeather
                .append(divFiveDayWeather
                    .append(contDaysWeather
                        .append(pDate,pDay,divContIcon,pTemp))))
})