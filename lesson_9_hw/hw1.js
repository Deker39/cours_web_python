function one_exer(){
    num1 = prompt("Введи первое число") 
    num2 =  prompt("Введи второе число") 
    if (num1 > num2) {
        alert(1)
    }
    else if (num1 < num2) {
        alert(-1)
    } 
    else if (num1 == num2){
        alert(0)
    }
    else {alert("Это не числа")}
}

function two_exer(){
    num1 = prompt("Введи факториал") 
    factorial = 1;
    for(i=2; i<=num1; i++)
     factorial *= i;
    alert(num1 + "! = " + factorial)
}
function three_exer(){
    num1 = prompt("Введи первую цифру") 
    num2 = prompt("Введи вторую цифру") 
    num3 = prompt("Введи третью цифру") 
    alert(num1 + num2 + num3)
}
function four_exer(){
    width = prompt("Введи длину прямоугольника") 
    height = prompt("Введи высоту  прямоугольника") 
    if (height == 0){
        alert("Площадь квадрата S = "+ width*width)
        
    } else
    if (width == 0){
        alert("Площадь квадрата S = "+ height*height)
        
    }
    else{alert("Площадь прямоугольника S = "+ width*height)}
    
}
function five_exer(){
    num1 = Number(prompt("Введи своё совершенное число"))
    let j = 0;
    for(let i=1;i<=num1/2;i++) {
          if(num1%i === 0) {
             j += i;
           }
      }
   
      if(j === num1 && j !== 0) {
        alert("Это совершенное число. " + num1);
         }  
       else {
        alert("Это не совершенное число. " + num1);
         }  
   
}
function six_exer(){
    function mini_five_exer(num1){
        let j = 0;
        for(let i=1;i<=num1/2;i++) {
            if(num1%i === 0) {
                j += i;
            }
        }
    
        if(j === num1 && j !== 0) {
            alert("Это совершенное число. " + num1);
            }  
    }
    range_min = Number(prompt("Введи своё минимальное число"))
    range_max =Number(prompt("Введи своё максимальное число"))
    for(i = range_min;i<=range_max;i++){
        mini_five_exer(i)  
    }
}
function seven_exer(){
    hour = prompt("Введи часы",'00')
    minut = prompt("Введи минуты",'00')
    second = prompt("Введи секунды",'00')
    if (hour==0 && minut == 0 && second == 0){ //если пользователь удалит наши нули
        hour = '00'
        minut = '00'
        second = '00'
        alert('Время сейчас ' + hour + ':' + minut + ':' + second )
    }else 
    if (hour == 0){
        hour = '00'
        alert('Время сейчас ' + hour + ':' + minut + ':' + second )
    } else
    if (minut == 0){
        minut = '00'
        alert('Время сейчас ' + hour + ':' + minut + ':' + second )
    } else
    if (second == 0){
        second = '00'
        alert('Время сейчас ' + hour + ':' + minut + ':' + second )
    } else
    alert('Время сейчас ' + hour + ':' + minut + ':' + second )
    

}
function eight_exer(){
    hour = Number( prompt("Введи часы",'00'))
    minut = Number(prompt("Введи минуты",'00'))
    second = Number(prompt("Введи секунды",'00'))
    alert(hour*60**2 + minut*60 + second + "с.")
}
function nine_exer(){
    second = Number(prompt("Введи секунды",'00'))
    var hours = Math.floor(second / 60 / 60)
    var minut = Math.floor(second / 60 )- (hours * 60)
    var seconds = second % 60
    alert(hours + ':' + minut + ':' + seconds);
}
function ten_exer(){
    data1 = prompt('Пример: December 17, 1995 03:24:00 \n Введите первую дату')
    data2 = prompt('Пример: December 20, 1995 03:24:00 \n Введите вторую дату')
    first_date = new Date(data1)
    second_date = new Date(data2)
    milisec = second_date - first_date
    alert("Всего секунд " + milisec/1000)
    var hours = Math.floor(milisec / 60 / 60 / 1000)
    var minut = Math.floor(milisec / 60 / 1000 ) - (hours * 60)
    var seconds = milisec % 60 
    alert("Всего часов: \n" + hours + ' : ' + minut + ' : ' + seconds);
}
ten_exer()