let form = document.querySelector('#form'),
    inputTitle  = document.querySelector('#titleId'), 
    inputType  = document.querySelector('#typeId'),
    formInputs = document.querySelectorAll(".form-control"),
    sectFirst = document.querySelector('#section-first'),
    btnSearch = document.querySelector('#search')
    token = '55f2a631',
    arrayMovies = []

let textList = document.createElement('h2'),
    sectMovieList = document.createElement('section')
    
    textList.innerHTML = 'Films'
    textList.classList.add('d-flex','justify-content-center')
    sectFirst.appendChild(textList)  


function creatDetailMovie(){

}
function creatListMovies(img,name,type,year) {

    
    sectMovieList.classList.add('container', 'mb-5', 'd-flex', 'flex-wrap')
    document.body.appendChild(sectMovieList)

    
        var contMovieItem = document.createElement('div'),
            contImg = document.createElement('div'),
            contTextItem = document.createElement('div'),
            textType = document.createElement('p'),
            textName = document.createElement('p'),
            textYear = document.createElement('p'),
            btnDetails = document.createElement('button')
        
        sectMovieList.appendChild(contMovieItem)
        contMovieItem.appendChild(contImg)
        contMovieItem.appendChild(contTextItem)
        contTextItem.appendChild(textType)
        contTextItem.appendChild(textName)
        contTextItem.appendChild(textYear)
        contTextItem.appendChild(btnDetails)

        contMovieItem.classList.add('d-flex', 'flex-row',  'mb-3', 'border', 'ms-3', 'bg-light')
        contImg.classList.add('m-2')
        contTextItem.classList.add('m-2', 'position-relative')
        textName.classList.add('fw-bold')
        btnDetails.classList.add('btn', 'btn-firts', 'btn-primary', 'position-absolute', 'bottom-0', 'end-0')
        
        contMovieItem.style.width = "320px"
        contMovieItem.style.height = "270px"
        contImg.style.minWidth  = "150px"
        contImg.style.height = "250px"
        if(img == 'N/A'){
            contImg.style.background = `url(no_film.png) center/cover no-repeat`
            
        }else{
            contImg.style.background = `url(${img}) center/cover no-repeat`
        }
       
        textType.innerText = `Type: ${type}`
        textName.innerText = `Title: ${name}`
        textYear.innerText = `Year made: ${year}`
        btnDetails.textContent = 'Details'

        btnDetails.addEventListener('click', function(e){
            detailRequest(name)// add url
        });
        // btnDetails.onclick = detailRequest(name)
    }

function detailRequest(name){
    let request
    url = `https://www.omdbapi.com/?t=${name.replace(/ /g,'+')}&apikey=${token}`
    console.log(url);
    if (window.XMLHttpRequest) {
        request = new XMLHttpRequest();
    }
    else {
        request = new ActiveXObject("Microsoft.XMLHTTP");
    }
    request.open('GET', url)
    request.responseType = "json";
    if (request.readyState === 4 &&request.status == 200) {
        let person = request.response;
        console.log(person);
        
        
    }

request.send();
return false
}

form.onsubmit = function(){
    let titleValue = inputTitle.value.toLowerCase(),
        typeValue = inputType.value.toLowerCase(),
        request

    url = `https://www.omdbapi.com/?s=${titleValue.replace(/ /g,'+')}&sype=${typeValue}&apikey=${token}`
    // console.log(url);
    
    if (window.XMLHttpRequest) {
        request = new XMLHttpRequest();
    }
    else {
        request = new ActiveXObject("Microsoft.XMLHTTP");
    }
    request.open('GET', url)
    request.responseType = "json";
    request.onload = function () {
        if (request.readyState === 4 &&request.status == 200) {
            let person = request.response;
            for(var i = 0; i < person['Search']['length']; i++){
                creatListMovies(person['Search'][i]['Poster'],person['Search'][i]['Title'],
                                person['Search'][i]['Type'],person['Search'][i]['Year'])//creatListMovies(img,name,type,year)
            }
            
        }
    }
    request.send();
    return false
}

// btnSearch.onclick  = function(){
//    if (arrayMovies.length > 0){

//     textList.innerHTML = 'Films'
//     textList.classList.add('d-flex','justify-content-center')
//     sectFirst.appendChild(textList)  


//     }else{
//         textList.innerHTML = 'Sorry, no such movie'
//         textList.classList.add('d-flex','justify-content-center')
//         sectFirst.appendChild(textList)
//     }
//     // console.log(arrayMovies);
//     // console.log(arrayMovies.length);
// }




