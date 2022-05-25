// if ( умова ) {
//
// }

// var age = prompt(">18?");
// if (age >= 18) {
//     alert("OK");
// }  
// else {
//     alert("No")
// } 
// var age = prompt("Enter your age: ")
// if (age % 2 == 0) {
//     alert("Congratuations!");
// }

// && - i, || - або,  ! - ні

// True && True -> True

// True || False - > True

// False || False -> False

//console.log(n>n1 && !n ==-1 || n>5 && !n);
// 1

// var age = ""
// if (age < 14 && age > 0) {
//     console.log("Child");
// } else if (age >= 14 && age <= 17) {
//     console.log("Teenager")
// } else if (age >= 65) {
//     console.log("Pensioner")
// }  else if (age >= 18) {
//     console.log("Adult")
// } else {
//     console.log("Error");
// }

// var num1 = 15
// var num2 = 100
// var num3 = 50
// if (num1>num2 && num1>num3){
//     console.log(num1);
// } else if (num2 > num3){
//     console.log(num2);
// } else {
//     console.log(num3);
// }

// (age>5) ? True : False ;
// console.log(
//     (num1>num2 && num1>num3)? num1 : 
//     (num2 > num3) ? num2 : num3);

// switch (value) {
//
//   case "BC": {
//      code...
//      break;
//   }    
//   
//   default: {
//      code..
//   }
//}
// var key = "WA";

// switch (key) {
//     case "AA": {
//         console.log("AA");
//         break;
//     }
//     case "BC":
//     case "BC":
//         console.log("BC");
//         break;
//     case "TA":
//         console.log("TA");
//         break;
//     default:
//         console.log("Unknown");
// }

// while (cond) {
//      code..
// }

// var i = 1
// var j = 1

// while (i<=10) {
//     j=1
//     while (j<=10) {
//         document.writeln("  "+i*j)
//         j+=1
//     }
//     document.write("<br>")
//     i+=1
// }
// while (false) {
//     console.log('1');
// }

// do {
//     console.log('2');
// } while (false);

// continue, break;


// for(pre-cond ; cond; after) {

// }


// for(let i=1, sum=0; i<=5; i++) {

// }

// var, let, const


// function iмя () {
        //..
// }

// let n1 = 5;
// let n2= 10;

// function foo(num1, num2) {
//     return (num1>num2) ? num1 : num2
// }

// let result = foo(n1,n2)

// console.log(result);

// function logArguments() {
//     console.log(arguments[3]);
// }

// logArguments(1,2,3,4)
// factorial  !5 = 1*2*3*4*5 = 120
// let f = 1;
// for (let i = 1; i <= 5; i++) {
//     f*=i;
// }

// console.log(f);
//1. return !
//2. args
// function foo(n) {
//     if (n == 1)
//         return 1;
//     return n*foo(n-1);
// }

// console.log(foo(5));

//var user1 = new Object();
// state & methods
// var age = 20

// var user1 = {age};
// user1["name"] = 'Alex'
//console.log(user2, user2.name);

// var user = {
//     name : 'John',
//     age : 35,
//     dislocation : {
//         city: 'Lviv'
//     },
//     show : function() {
//         console.log(this.name, this.age);
//     }
// }
// console.log(user1, user1.name,  user1['name']);

// delete user1.age

// if ("age" in user1) {
//     console.log('yes');
// } else {
//     console.log('no');
// }

// user1.show()

// for (const key in user) {
//     console.log(key, user[key]);
// }
// console.log(typeof(user));

// var arr = new Array();
// var arr = [];

// var arr = [];

// arr[0]=50
// arr[1]=10
// console.log(arr);

// var arr = new Array(2, 5, 7, true, "123", 6);

// console.log(arr.length);

// arr.length = 0
// arr.length = 5
// console.log(arr);

//var arr = [3.0003, 5, 9.232, -45.123213];
// arr.push(5,7)

// console.log( arr.toString())
// var result = arr.map(item => {
//   return item.toFixed(2)
// });

// var arr = [
//     [1,2,3],
//     [4,5,6]
// ]

// for (let i = 0; i < arr.length; i++) {
//     for (let j = 0; j < arr[i].length; j++) {

//     }
// }
// console.log( arr[1].indexOf(6));
// arr.sort()
// \t - tab , \n - newline, \\ - \, \"-  "
// var line = "Lorem"
// console.log(line);
// console.log(line[7]);
// line[0]='A'
// console.log(line);
// console.log(line.length)
// console.log(line.charAt(0),line[-5])
// console.log(line.toLocaleUpperCase(), line);
// console.log(line.slice(0,5))
// console.log(line.localeCompare("lorem") == 0)




// setTimeout(function(a,b) {
//     console.log("Hello");
//     console.log( a+b)
// }, 100000, 5, 10)
 
// var id = setInterval(test, 2000)
// var i = 0
// function test() {
//     if (i == 5){
//         clearInterval(id)
//         console.log('Interval stoped');
//     }
//     i++;
// }

// console.log(Math.random());
// 1-10
// console.log();
// let arr = new Array()
// for (let i = 0; i < 10; i++) {
//     arr.push(Math.round((Math.random()*10)))  
//     console.log(arr[i]);  
// }

// console.log(Math.sqrt(16), Math.pow(2,3), Math.abs(-5));

// let day = prompt("Enter day: ")
// let month = prompt("Enter month: ")
// let year = prompt("Enter year: ")

// let bd = new Date(day+"/"+month+"/"+year)
// let now = new Date()
// let ms = now - bd
// console.log("Age: "+(now.getFullYear()-Number(year)), ms);
// let now = new Date()

// console.log(now.toLocaleString()); 
// console.log(now);
// console.log(now.toLocaleDateString());
// console.log(now.toLocaleTimeString());


// let number = 12.3456
// console.log(number.toLocaleString());
// console.log(new Array());
// console.log(typeof(Date), Date);

// function createPerson(name, age) {
//     this.name = name;
//     this.age = age;
//     this.show = function() {
//         console.log("Name: "+this.name+"Age: "+this.age);
//     };
// }

// let obj1 = {
//     name: 'Alex',
//     age: 21,
//     show: function(){
//         console.log("Name: "+this.name+"Age: "+this.age);
//     }
// }

// let obj2 = {
//     name: 'John',
//     age: 30,
//     show: function(){
//         console.log("Name: "+this.name+"Age: "+this.age);
//     }
// }

// let obj3 = new createPerson("Den",23);

// console.log(obj1, obj2, obj3);

// obj1.show()
// obj2.show()

// class Person {

//     #name;
//     #age;
//     #live;
//     static #percentageRate = 15
//     constructor(name, age, live){
//         console.log("Call Constructor");
//         this.#name = name;
//         this.#age = age;
//         this.#live = live;
//     }

//     work(place){
//         console.log(`Person going to ${place}`);
//     }

//     move(){
//         console.log("He move");
//     }

//     show(){
//         console.log(
//             `Name: ${this.#name}, 
//             Age: ${this.#age}, 
//             Live: ${this.#live}`);
//     }

//     static show(person) {
//         console.log(
//             `Name: ${person.#name}, 
//             Age: ${person.#age}, 
//             Live: ${person.#live}
//             PRate: ${this.#percentageRate}`);
//     }

//     get data() {
//         return this.#name + ' ' +this.#age;
//     } 
    
//     set data(value) {
//         [this.#name, this.#age] = value.split(" ");
//     } 

//     static percentageRate() {
//         return this.#percentageRate;
//     }

//     validateAge(age) {
//         if (age<0 || age>150)
//             return true;
//         return false;
//     }

// }
// //Наследование
// // let obj1 = new Person("John", 30, true);
// // let obj2 = new Person("Den", 12, true);


// class Empoyer extends Person{

//     #salary
//     constructor(name, age, live,salary){
//         console.log('Emp');
//         super(name, age, live)
//         this.#salary = salary
//     }
    
//     show(){

//         console.log(`
//             Name: ${super.name}, 
//             Age: ${super.age}, 
//             Live: ${super.live}
//             Salary: ${this.#salary}`
//         );
//     }
// }

// let p2 = new Empoyer("John", 30, true, 1234)
// p2.show()


// function foo(value) {
//     console.log(value.type);
// }
// var elem = document.getElementById('d1')
// document.getElementById('d1').addEventListener('click',foo)

// function foo(value) {
//     console.log(value.type);
// }
// document.getElementById('d1').onclick = foo

// var clicks = 0
// var colors = ['red','green','blue','yellow']
// function handler(e){
//     clicks++
//     var elem = document.getElementById('p1')
//     elem.innerText = clicks
//     elem.style.backgroundColor = colors[Math.round(Math.random()*colors.length)]
//     // elem.append(clicks)
// // }
// var map  = document.getElementById("img1")

//     var HEIGHT = map.clientHeight
//     var WIDTH = map.clientWidth

// var treasure ={
//     "X":Math.round(Math.random()*WIDTH),
//     "Y":Math.round(Math.random()*HEIGHT)
// }
// setTimeout(pause,1000)
// console.log(treasure)
// function handler(e){
//     var elem = document.getElementById('p1')
//     elem.innerHTML = "x:" + e.clientX + "<br>Y:" + e.clientY
//     // document.body.appendChild(newNode)
//     // var elem = document.getElementById('p1')
//     // elem.innerHTML = 'Tag name: ' + e.target.nodeName
//     // elem.innerHTML = `X: ${e.clentX}`
// }
// var block = document.getElementById('b1')
// block.addEventListener('click',handler)


// const selectElement = document.querySelector("#inp")

// selectElement.addEventListener('input',function(e){
    
//     console.log(e);
// })
// function foo(tag){
//     console.log(tag);
// }

// menu.onclick = function(event) {
//     if (event.target.nodeName != 'A') return;
  
//     let href = event.target.getAttribute('href');
//     alert( href ); // может быть подгрузка с сервера, генерация интерфейса и т.п.
  
//     return false; // отменить действие браузера (переход по ссылке)
//   };
// var an = (a,b) => a+b
// var s = new Array()
// s.map(item => item*2).
// console.log(an);
// document.body.onkeydown = (e) => {
//     if(e.shiftKey || e.ctrlKey) e.preventDefault()
//     document.body.addEventListener('click',  (e) =>{
//         console.log(e)
//     })

//     document.body.oncontextmenu = (e) => e.preventDefault()

// }
// var v = 0
// var l = 0
// var d = document.getElementById("div1")
// document.body.onkeydown = (e) => {
//     if(e.key =='s') {
//         v += 5 
//         d.style.top = v + 'px'
//     }else
//     if(e.key =='w') {
//         v -= 5 
//         d.style.top = v + 'px'
//     }else
//     if(e.key =='a') {
//         l += 5 
//         d.style.left = l +'px'
//     }else
//     if(e.key =='d') {
//         l -= 5 
//         d.style.left = l +'px'
//     }

// }
var words = [
    'hello',
    'world',
    'python',
    'prog',
    'jsckript'
]
var word = words[Math.floor(Math.random()*words.length)]
var lines = '_'.repeat(word.length).split('')
var tryes
console.log(lines);
var ph = document.getElementById('bin')
var answer
function game(e){
    document.getElementById('guess').innerHTML= lines.join(' ')
    console.log(ph.textContent);
    if(e !== undefined ){
        if (!ph.textContent.includes(e.key)){
        ph.append(e.key + '')
    }
    }
   
    if(e.key){
        for (let i = 0; i < word.length; i++) {
            if(e.key === word[i]){
                lines[i] = e.key
            }
            
        }
        if(answer === word.toString()){
            lines = word.split('')
            alert(`you win, your tryes: ${tryes}`)
            
        }
        
    }
    tryes++
   
}
document.body.onkeydown = (e) => game(e)

window.onload = game()




