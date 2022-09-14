//promt()
//alert()
function one_exer(){
    let kek = Number(prompt("Введи число"))
    alert("Степень вашего числа = " + kek**2)
}
function two_exer(){
    let kek1 = Number(prompt("Введи число 1"))
    let kek2 = Number(prompt("Введи число 2"))
    alert("Среднее арефметическое двух = " + (kek1+ kek2)/2)
}
function three_exer(){
    let kek = Number(prompt("Введи сторону квадрата"))
    alert("Площадь квадрата = "+kek**2)
}
function four_exer(){
    let kek = Number(prompt("Введите километры"))
    let result= kek*0.621371
    alert("В милях это примерно= "+ Math.ceil(result))
}
function five_exer(){
    let kek1 = Number(prompt("Введи число 1"))
    let kek2 = Number(prompt("Введи число 2"))
    let result_plus = kek1 + kek2
    let result_minus = kek1 - kek2
    let result_multiply = kek1 * kek2
    let result_divide = kek1 / kek2
    alert("Сумма "+ result_plus + "\n" +
          "Разность "+ result_minus + "\n" +
          "Произвидение "+ result_multiply + "\n" +
          "Частное "+ result_multiply
        )
}
function six_exer(){
    let kek1 = Number(prompt("Введи число a"))
    let kek2 = Number(prompt("Введи число b"))
    let result = (-kek2)/kek1
    alert("a*x+b=0 нужно найти X \n"+ "x ="+ result)
}
function seven_exer(){
    let kek1 = Number(prompt("Введи сколько часов"))
    let kek2 = Number(prompt("Введи сколько минут"))
    let now = new Date().toLocaleTimeString().slice(0,-3)
    let result1 = 23-kek1 
    let result2 = 60-kek2
    alert( result1+":"+ result2);
}
function eight_exer(){
    let kek1 = Number(prompt("Введи трехзначное число"))
    letresult = Math.floor(kek1/10)%10
    alert("Второе число " + result)
}
function nine_exer(){
    let kek1 = prompt("Введи пятизначное число")
    let result1 = kek1%10
    let result2 = Math.floor(kek1/10)
    alert(result1 + "" + result2)
}
function ten_exer(){
    let kek =  prompt("Общаяя сумма продаж за месяц")
    let result = 250 + (kek * 0.1)
    alert("Ваша зарплата " + result + "$")
}
// one_exer()
// two_exer()
// three_exer()
// four_exer()
// five_exer()
// six_exer()
// seven_exer()
// eight_exer()
// nine_exer()
// ten_exer()