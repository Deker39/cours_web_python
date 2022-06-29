let arr_weather = ''

$.ajax({
    url: 'http://api.weatherstack.com/current',
    data: {
        access_key: '2a25e079cb1c98bb8a9ae458589cece2',
        query: 'Odesa'
    },
    dataType: 'json'
    }).done(function (data) {
    console.log(data);
    // $.each(data.current, function (index, currentInfo) {
    //     console.log(`${index}: ${currentInfo}`);
    // })
    // $.each(data.location, function (index, currentInfo) {
    //     console.log(`${index}: ${currentInfo}`);
    // })
    // $.each(data.location, function (index, currentInfo) {
    //     console.log(`${index}: ${currentInfo}`);
    // })
            })

