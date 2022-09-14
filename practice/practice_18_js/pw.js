/*-------------------------------------------------*/
const numb = document.getElementById('numb')

numb.addEventListener('keydown', e => e.preventDefault())

/*-------------------------------------------------*/

const addColor = document.getElementById('btnAddColor')
const contBlock = document.getElementById('contBlock')

addColor.onclick = function(){
    const divColor = document.createElement('div')
    divColor.classList.add('box')
    divColor.style.backgroundColor = `#${(Math.random().toString(16) + '000000').substring(2,8).toUpperCase()}`

    contBlock.appendChild(divColor)
}
contBlock.addEventListener('click', event =>{ event.target == event.currentTarget? false: event.target.remove() })
/*-------------------------------------------------*/

const palitra = document.getElementById('palitra')


for(var i = 0; i < 20; i++){
     const divBlockPalit  = document.createElement('div')
     divBlockPalit.classList.add('s-box')
     divBlockPalit.classList.add('col')
     divBlockPalit.classList.add('border')
     divBlockPalit.style.backgroundColor = `#${(Math.random().toString(16) + '000000').substring(2,8).toUpperCase()}`
     palitra.appendChild(divBlockPalit)
}


// document.querySelectorAll('#palitra div')
palitra.addEventListener('click', event =>{
    event.target == event.currentTarget? false:  document.getElementById('text').style.color = event.target.style.backgroundColor
   
})

/*-------------------------------------------------*/
const form = document.querySelector('#form'),
     formInputs = document.querySelectorAll("#form .form-control"),
     contComent = document.getElementById('contComent'),
     inputName = document.getElementById('textName'),
     inputComment = document.getElementById('textComment')

var  array = []
var  kek = 0

function writeComment(name, time, comment){

    const div = document.createElement('div')
    const pName = document.createElement('h5')
    const pDate = document.createElement('p')
    const pComment = document.createElement('h5')

    div.classList.add('shadow','p-3','mb-3','bg-info','bg-gradient','bg-opacity-25','rounded')

    pName.innerHTML = name
    pDate.innerHTML = time
    pComment.innerHTML = comment

    contComent.appendChild(div)
    div.appendChild(pName)
    div.appendChild(pDate)
    div.appendChild(pComment)

}

function Comment(name,time,comment){
    this.name = name
    this.time = time
    this.comment = comment
}

form.onsubmit = function () {
    
    formInputs.forEach(function (input){
        if(input.value === '' || input.value === ' '){
            input.classList.add('is-invalid')
            return false
        }else{
            input.classList.remove('is-invalid')
        }
        
    });
   
    if (!inputName.value && !inputComment.value || !inputName.value && inputComment.value || inputName.value && !inputComment.value) {
        return false
    } else {
        array.push(new Comment(inputName.value,new Date().toLocaleDateString(),inputComment.value))
        localStorage.getItem('count') === null? kek = 0:kek = localStorage.getItem('count')
        localStorage.setItem(`array${kek}`, JSON.stringify(array))
        kek++
        localStorage.setItem(`count`,kek)
    }
}

var c = localStorage.getItem('count')

for (let i = 0; i <= c; i++) {
    writeComment(JSON.parse(localStorage.getItem(`array${i}`))[0]['name'],
    JSON.parse(localStorage.getItem(`array${i}`))[0]['time'],
    JSON.parse(localStorage.getItem(`array${i}`))[0]['comment'])
}

/*-------------------------------------------------*/
const contCount = document.getElementById('contCount')
const countryList = document.getElementById('countryList')

var word = new String(),
    count = 0 

var country = [
    'Афганистан','Албания','Антарктика','Алжир','Американское Самоа','Андора','Ангола','Антигуа и Барбуда','Азербайджан','Аргентина','Австралия',
    'Австрия', 'Багамские Острова','Бахрейн','Бангладеш','Армения','Барбадос','Бельгия','Бермудские Острова','Бутан','Боливия','Босния и Герцеговина',
    'Ботсвана','Остров Буве','Бразилия','Белиз','Британская территория в Индийском океане','Соломоновы Острова','Британские Виргинские острова',
    'Бруней','Болгария','Мьянма','Бурунди','Белоруссия','Камбоджа','Камерун', 'Канада','Кабо-Верде','Каймановы острова',
    'Центральноафриканская Республика', 'Шри-Ланка','Чад','Чили','Китайская Народная Республика','Остров Рождества','Кокосовые острова','Колумбия', 'Коморы','Майотта',
    'Республика Конго', 'Демократическая Республика Конго','Острова Кука','Коста-Рика','Хорватия','Куба','Кипр','Чехия','Бенин', 'Дания','Доминика',
    'Доминиканская Республика','Эквадор','Сальвадор','Экваториальная Гвинея','Эфиопия','Эритрея','Эстония','Фарерские острова','Фолклендские острова',
    'Южная Георгия и Южные Сандвичевы острова','Фиджи','Финляндия','Аландские острова','Франция','Французская Гвиана','Французская Полинезия',
    'Французские Южные и Антарктические территории','Джибути','Габон','Грузия','Гамбия','Палестина','Германия','Гана','Гибралтар','Кирибати',
    'Греция','Гренландия','Гренада','Гваделупа','Гуам','Гватемала','Гвинея','Гайана','Республика Гаити','Остров Херд и острова Макдональд','Ватикан',
    'Гондурас','Гонконг','Венгрия','Исландия','Индия','Индонезия','Иран', 'Ирак','Ирландия','Израиль', 'Италия', 'Кот-д’Ивуар','Ямайка','Япония',
    'Казахстан','Иордания','Кения','КНДР','Республика Корея','Кувейт', 'Киргизия','Лаос','Ливан','Лесото','Латвия','Либерия','Ливия', 'Лихтенштейн',
    'Литва','Люксембург', 'Макао', 'Мадагаскар', 'Малави','Малайзия', 'Мальдивы' ,'Мали','Мальта','Мартиника','Мавритания','Маврикий','Мексика',
    'Монако','Монголия','Молдавия','Черногория','Монтсеррат','Марокко','Мозамбик','Оман','Намибия','Науру','Непал','Нидерланды','Кюрасао','Аруба',
    'Синт-Мартен','Бонэйр, Синт-Эстатиус и Саба','Новая Каледония','Вануату', 'Новая Зеландия', 'Никарагуа', 'Нигер', 'Нигерия', 'Ниуэ', 'Норфолк', 'Норвегия',
    'Северные Марианские острова', 'Внешние малые острова США', 'Микронезия','Маршалловы Острова','Палау','Пакистан','Панама',
    'Папуа — Новая Гвинея','Парагвай', 'Перу', 'Филиппины', 'Острова Питкэрн','Польша','Португалия','Гвинея-Бисау','Восточный Тимор','Пуэрто-Рико',
    'Катар','Реюньон','Румыния','Россия','Руанда','Сен-Бартелеми','Острова Святой Елены',' Вознесения и Тристан-да-Кунья',
    'Сент-Китс и Невис','Ангилья','Сент-Люсия', 'Сен-Мартен (Франция)','Сен-Пьер и Микелон','Сент-Винсент и Гренадины','Сан-Марино',
    'Сан-Томе и Принсипи','Саудовская Аравия', 'Сенегал','Сербия','Сейшельские Острова','Сьерра-Леоне','Сингапур','Словакия','Словения','Сомали',
    'Южно-Африканская Республика','Зимбабве','Испания','Южный Судан','Судан','Западная Сахара','Суринам','Шпицберген и Ян-Майен','Свазиленд','Швеция',
    'Швейцария','Сирия','Таджикистан','Таиланд','Того','Токелау','Тонга','Тринидад и Тобаго','Объединённые Арабские Эмираты','Тунис',
    'Турция','Туркмения','Теркс и Кайкос','Тувалу','Уганда','Украина','Республика Македония','Египет','Великобритания','Гернси','Джерси','Остров Мэн',
    'Танзания','Соединённые Штаты Америки','Виргинские Острова','Буркина-Фасо','Уругвай','Узбекистан','Венесуэла','Уоллис и Футуна','Самоа','Йемен','Замбия',
];

let datalist = document.createElement('datalist')
datalist.setAttribute('id', 'datalistCount')
contCount.appendChild(datalist)

function search(elem) {
   
   if(count < 10){
    let opt = document.createElement('option')
    datalist.appendChild(opt)
    opt.value = elem 
    count++
   }
    
    
    
}

countryList.addEventListener('keypress', event =>{
    word += event.key
    
    while (datalist.firstChild) {
        datalist.removeChild(datalist.firstChild);
        count = 0
    }

    country.forEach(element => {
        element.slice(0,word.length).toLowerCase() == word.toLowerCase()? search(element) : false
    });
    
    
    
})
countryList.addEventListener('keydown', event =>{
    if(event.key == "Backspace"){
        
        word = word.slice(0,-1)
        while (datalist.firstChild) {
            datalist.removeChild(datalist.firstChild); 
            count = 0
        }
        
        country.forEach(element => {
            element.slice(0,word.length).toLowerCase() == word.toLowerCase()? search(element) : false
        });
    }
    else false 

})