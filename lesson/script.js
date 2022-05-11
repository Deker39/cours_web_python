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
var id  = setInterval(test, 2000)
var i =0 
function test(){
    if(i == 5){
        clearInterval(id)
        console.log('interval stoped')
    }
    i++
    
}