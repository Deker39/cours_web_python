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
function foo(n){
    if(n==1)
        return 1
    return n*foo(n-1)
}

console.log(foo(5)); 