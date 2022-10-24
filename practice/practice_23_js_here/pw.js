var arrayTitleFruits = ['Mango','Orange','Pineapple','Papaya','Greapefruit','Pear']
var arrayImagesFruiys = ['image/mango.webp','image/orange.jpg','image/pineapple.webp','image/papaya.jpg','image/greapefruit.jpg','image/pear.jpg']
var arrayDescriptionFruits = [
    'A mango is an edible stone fruit produced by the tropical tree Mangifera indica. It is believed to have originated in the region\
    between northwestern Myanmar, Bangladesh, and northeastern India. M. indica has been cultivated in South and Southeast Asia\
    since ancient times resulting in two types of modern mango cultivars: the "Indian type" and the "Southeast Asian type".\
    Other species in the genus Mangifera also produce edible fruits that are also called "mangoes", the majority of which are found\
    in the Malesian ecoregion.',
    'An orange is a fruit of various citrus species in the family Rutaceae (see list of plants known as orange); it primarily refers\
    to Citrus sinensis, which is also called sweet orange, to distinguish it from the related Citrus aurantium, referred to\
    as bitter orange. The sweet orange reproduces asexually (apomixis through nucellar embryony); varieties of sweet orange arise\
    through mutations.',
    'The pineapple (Ananas comosus) is a tropical plant with an edible fruit; it is the most economically significant plant in the\
    family Bromeliaceae. The pineapple is indigenous to South America, where it has been cultivated for many centuries. The\
    introduction of the pineapple to Europe in the 17th century made it a significant cultural icon of luxury. Since the 1820s\
    , pineapple has been commercially grown in greenhouses and many tropical plantations.',
    'The papaya is the plant Carica papaya, one of the 22 accepted species in the genus Carica of the family Caricaceae. It was\
    first domesticated in Mesoamerica, within modern-day southern Mexico and Central America. In 2020, India produced 43% of the\
    world supply of papayas.',
    'The grapefruit is a subtropical citrus tree known for its relatively large, sour to semi-sweet, somewhat bitter fruit. The\
    interior flesh is segmented and varies in color from pale yellow to dark pink. Grapefruit is a citrus hybrid originating in\
    Barbados. It is an accidental cross between the sweet orange (C. sinensis) and the pomelo or shaddock (C. maxima), both of\
    which were introduced from Asia in the 17th century. It has also been called the forbidden fruit. In the past it was referred\
    to as the pomelo, but that term is now mostly used as the common name for Citrus maxima.',
    'Pears are fruits produced and consumed around the world, growing on a tree and harvested in the Northern Hemisphere in late\
    summer into October. The pear tree and shrub are a species of genus Pyrus, in the family Rosaceae, bearing the pomaceous fruit\
     of the same name. Several species of pears are valued for their edible fruit and juices, while others are cultivated as trees.'

]

function creatDescription(index){
    if($('#descriptionFruit').length){
        $('#imageFruit').attr('src',arrayImagesFruiys[index])
        $('#titleFruit').text(arrayTitleFruits[index])
        $('#textFruit').text(arrayDescriptionFruits[index])
    }else{
        $('<div class="d-flex justify-content-center align-items-center" id="descriptionFruit">' +
        `<img class="m-2" src="${arrayImagesFruiys[index]}" alt="" width="150px" height="150px" id="imageFruit">`+
        '<div class="m-2">'+
            `<h5 class="text-center" id="titleFruit">${arrayTitleFruits[index]}</h5>`+
            `<p id="textFruit">${arrayDescriptionFruits[index]}</p>`+
        '</div>'+
      '</div>').appendTo('#navbar')
    }

}


$().ready(function(){
    $('#frutisNavBar li:first-child a').addClass('active')
    creatDescription(0)
})
$('#frutisNavBar').on('click',function(event){
    if($('#frutisNavBar .active').length){
        $('#frutisNavBar .active').removeClass('active')
        $(event.target).addClass('active')
        creatDescription([].indexOf.call(this.children, $(event.target).parent().get(0)))
    }
})


