// console.log('kek')
// var age = prompt(">18")
// if (age >= 18) {
//     alert('ok')
// } else {
//     alert("no")
// }
// var age = prompt("Enter your age?")
// if (age % 2 == 0){
//     alert('he')
// }
// else{

// }
// var age = prompt("Enter your age?")
// if (age <= 14 && age > 0) {
//     alert('child')   
// } else if ( age <= 18) {
//     alert('Tennage')
// }if (age >= 18) {
//     alert('Adult')
// } else if(age >= 65){
//     alert("Pensioner")
// }
// else{
//     alert('false')
// }
// var key = "BC"
// switch (key) {
//     case "AA":
//         console.log('kiey');
//         break
//     case "BC":
//     case "BC":
//         console.log();
//         console.log('lviv');
//         break
//     case "TA":
//         console.log("TA");
//         break
//     default:
// }
// var i = 1
// var j = 1
// while (i<=10) {
//     j=1
//     while (j<=10) {
//         document.write(i*j);
//         j+=1;
//     }
//     document.write('<br>')
//     i+=1;
// }
// do {
//     console.log('2');
// } while (false);
// var i =1
// while (i<=100) {
//     document.write(i+'<br>')
//     if(i==40)
   
//     break;
//     i+=1
    
// }
// for(var i=0,j=4; i<j && j!=0; i++){
//     document.write(i)
// }
// let n1 = 5
// let n2 = 10
// function kek(num1,num2) {
//     num1+=num2
//     num2*=2
//     document.writeln(num1+' '+num2);
//     return num2
// }
// document.writeln(kek(n1,n2))
// function foo(n){
//     if(n==1)
//         return 1
//     return n*foo(n-1)
// }

// console.log(foo(5)); 

// var user1 = new Object();
// var user1 = {
//     name: 'Jhon',
//     age : 35,
//     dislocation:{
//         city:'Lviv',
//         districk: 'Lvivs`ka'
//     },
//     show : function(){
//         console.log(this.name, this.age);
//     }
// }
// // console.log(user1 ,user1.name);

// for (const key in user1) {
//     console.log(key,user1[key])
// }
// user1.show()

// var arr = new Array();
// var arr = [];

// arr[0]=45
// arr[1]=50


// var kek = new Array(2,5,7, true,"123")
// console.log(kek[4])
// var arr = [2,4,5,6]
// arr.push(9)
// arr.toString

// console.log(arr.forEach);
// arr.forEach(item => {
//      item*2
// });

// console.log(arr);

// var arr = [
//     [1,2,3],
//     [4,5,6]
// ]
// var g =document.getElementById('m')

// console.log(arr);
// for(let i =0; i < arr.length; i++){
//     for(let j =0; j <= arr.length; j++){
    
//     g.innerHTML = arr[i][j];
//     }
// }

// var line = " lorem ipsum solod sit dor amet"
// function mess(a,b){
//     console.log('hello');
//     return a+b
// }
// setTimeout(mess, 2000, 5 ,10)
// var id  = setInterval(test, 2000)
// var i =0 
// function test(){
//     if(i == 5){
//         clearInterval(id)
//         console.log('interval stoped')
//     }
//     i++
    
// }
// console.log(Math.round(Math.random()*10)+1);
// let a  = []
// for(let i=0; i <= 10; i++){
//         a.push(Math.round(Math.random()*10))
//         console.log(a[i]);
// }
// let date_now = new Date()
// let date_old = new Date(date_now.getUTCFullYear()+"T13:13:11")
// console.log(date_now)
// console.log(date_now.valueOf())
// console.log(date_old.getHours() +":"+date_old.getMinutes() + ":"+ date_old.getSeconds());
// console.log(Date.parse(date_now))
// console.log(date_now.getTime());
// let now = new Date()
// console.log(now.toLocaleString());
// console.log(now);
// console.log(now.toLocaleDateString());
// console.log(now.toLocaleTimeString());

// function createPerson(name, age){
//     this.name = name;
//     this.age = age;
//     this.show = function(){
//         console.log('Name: ' + this.name + '\nAge: ' + this.age);
//     }
// }

// let obj1 = {
//     name: 'Alex',
//     age : 21,
//     show: function(){
//         console.log('Name: ' + this.name + '\nAge: ' + this.age);
//     }
// }


// let obj2 = {
//     name: 'Jhon',
//     age : 30,
//     show: function(){
//         console.log('Name: ' + this.name + '\nAge: ' + this.age);
//     }
// }
// let obj3 = new createPerson('Den',23)
// console.log(obj1,obj2,obj3);
// obj1.show()
// obj2.show()

// class Person{
//     // name = 'default';
//     // age = 'default';
//     #live;
//     #name;
//     #age;
//     constructor(name,age, live){
//         console.log('Call Construction');
//         this.#name = name;
//         this.#age = age;
//         this.#live = live
//     }
//     work(place){
//         console.log(`Person going to ${place}`);
//     }
//     move(){
//         console.log("He move");
//     }
//     name(){
//         return this.#name
//     }
//     setName(){
//         this.#name = name;
//     }
//     age(){
//         return this.#live
//     }
//     setAge(){
//         if(age < 0 || age > 150)
//             console.log('Unvalid age')
//         else
//             this.#age = age
//     }
// }

// let obj = new Person('jhon',40,true)
// // obj.name = 'alex'
// // obj.age = 23
// obj.work('oficce')
// obj.move()
// console.log(obj);

// function kek(){
//     // document.getElementById('demo').innerHTML = 'kek cheburek'
//     // document.getElementById('demo').style.backgroundColor = "red"
//     // document.getElementById('ul').style.display = "block"
//     // document.write(5+6)
//     // alert(2)
//     console.log(3%6);
// }

// console.log(document);
// let elem = document.documentElement.childNodes
// for (let i = 0; i < elem.length;i++ ){
//     document.write(`<p> ${i+1} ${elem[i].tagName} ${elem[i].nodeName} </p>`)
// }

// const  check = (e) => {
//     const form= e.currentTurget
//     let login= document.getElementById('email').value
//     if(login.length == 0){
//     alert('zero len')
//     return 0
//     }
//     document.getElementById('f1').submit()
// }
// let temp = new RegExp(/([0-3][0-1]|[1-2][0-9]|[0][0-9])\.([0][1-9]|[0-1][1-2])\.\d\d\d\d/gm)
//  console.log(temp.test('20.02.2020'));
//  console.log(temp.exec("20.02.2020"));
//  console.log("20.02.2020".match(temp));
//  let line = "Mon Jun 06 2022 21:01:25 GTM+0300"


 // let date = new Date()
    // console.log(date);
    // date.setMinutes(date.getMinutes()+1)
    // let name1 = 'Alex1'
    // let name2 = 'Alex2'
    // let name3 = 'Alex3'
    // document.cookie = `name1=${encodeURIComponent(name1)};expires=${date};`
    // document.cookie = `name2=${encodeURIComponent(name2)};expires=${date};`
    // document.cookie = `name3=${encodeURIComponent(name3)};expires=${date};`

    // console.log(document.cookie.split(';'));
    // let arr_cookie = document.cookie.split(';')
    // arr_cookie.forEach(item =>{
    //     let pair = item.split('='),
    //         key = pair[0]
    //         value = pair [1]
    //     console.log(`key: ${key}\tvalue: ${value}\t`);
    // }) 