function first(){
    let numb = Number(prompt('Enter your value'))
    if( numb == 0 ){ console.log(`your value zero: ${numb}`);}
    else if(numb < 0){console.log(`your value less than zero: ${numb}`);
    }else if(numb > 0){console.log(`your value greater than zero: ${numb}`);}
}

function second(){
    let age = Number(prompt('Enter your age'))
    if(age > 0 && age <= 120)
    { if(age <= 12) console.log(`you child :${age}`);
    if(age > 12 && age <= 21) console.log(`you teenager :${age}`);
    if(age > 21 && age <= 50) console.log(`you man :${age}`);
    if(age > 50) console.log(`you old man :${age}`);
    }else console.log(`your age is not true:${age}`);
}

function thrid(){
    let numb = Number(prompt('Enter your age'))
    console.log(`Your value of module: ${Math.abs(numb)}`);
}

function fourth(){
    let clock = prompt('Example: 12:12:12\nEnter your time')
    let clok_arr = clock.split(':')
    if (clok_arr[0] >= 0 && clok_arr[1] >= 0 && clok_arr[1] && clok_arr[2] < 60 && clok_arr[2] >= 0){
        console.log(`Your time is right: ${clock}`);
    }else console.log(`please, enter correct time: ${clock}`);

}

function fifth(){
    let coordinates = prompt('Enter x,y coordinates')
    let coordinates_arr = coordinates.split(',')
    if(coordinates_arr[0] > 0 && coordinates_arr[1] > 0 ) {
        console.log(`First quarter: x= ${coordinates_arr[0]} y= ${coordinates_arr[1]}`)
    }
    else if(coordinates_arr[0] < 0 && coordinates_arr[1] > 0 ){
        console.log(`Second quarter: x= ${coordinates_arr[0]} y= ${coordinates_arr[1]}`)
    }
    else if(coordinates_arr[0] < 0 && coordinates_arr[1] < 0 ){
        console.log(`Third quarter: x= ${coordinates_arr[0]} y= ${coordinates_arr[1]}`)
    }
    else if(coordinates_arr[0] > 0 && coordinates_arr[1] < 0 ){
        console.log(`Fourth quarter: x= ${coordinates_arr[0]} y= ${coordinates_arr[1]}`)
    }
    else if(coordinates_arr[0] == 0 && coordinates_arr[1] == 0 ){
        console.log(`the coordinates are on the axis: x= ${coordinates_arr[0]} y= ${coordinates_arr[1]} `)
    }
    else if(coordinates_arr[0] == 0 && coordinates_arr[1] != 0 ){
        console.log(`The coordinates are on the axis x: x= ${coordinates_arr[0]} y= ${coordinates_arr[1]} `)
    }
    else if(coordinates_arr[0] != 0 && coordinates_arr[1] == 0 ){
        console.log(`The coordinates are on the axis y: x= ${coordinates_arr[0]} y= ${coordinates_arr[1]} `)
    }

}

function sixth(){
    let month = Number(prompt('Enter number of month'))
    switch (month) {
        case 1:console.log('January');break;  
        case 2:console.log('February');break;  
        case 3:console.log('March');break;  
        case 4:console.log('April');break;  
        case 5:console.log('May');break;  
        case 6:console.log('June');break;  
        case 7:console.log('July');break;  
        case 8:console.log('August');break;  
        case 9:console.log('September');break;  
        case 10:console.log('October');break;  
        case 11:console.log('November');break;  
        case 12:console.log('December ');break;  
    }
}

function seventh(){
    let number = prompt('Enter your values: 2+2')
    let number_arr = number.split(/\+|\-|\*|\//)
    let sim
    for (var i =0;i<number.length;i++){
        if(number[i] == '+' || number[i] == '-' || number[i] == '*' || number[i] == '/'){
            sim = number[i]
        }
    }
    switch (sim) {
        case '+':
            console.log(Number(number_arr[0]) + Number(number_arr[1]))
            break;
        case '-':
            console.log(Number(number_arr[0]) - Number(number_arr[1]))
            break
        case '*':
            console.log(Number(number_arr[0]) * Number(number_arr[1]))
            break
        case '/':
            console.log(Number(number_arr[0]) / Number(number_arr[1]))
            break
      
    }
}

function eighth(){
    let n1 = prompt("Enter two value: 1,2")
    n1 = n1.split(',')
    console.log(n1[0] == n1[1] ? `They are equal` : 
                n1[0] > n1[1] ? `The first number is greater: ${n1[0]}` : `The second number is greater  ${n1[1]}`) 

}

function nineth(){
    let num = prompt("Enter your value")
    console.log(Math.floor(num%5));
    
    console.log( Math.floor(num%5)? `no ${num}, your number is not a multiple of 5`:`yes ${num}, your number is a multiple of 5`);
}

function tenth(){
    let name_planat = prompt('Enter name your planet')
    console.log(name_planat != 'Earth' ? 'hello, Alien':'hello, Earthling' );
}
// first()
// second()
// thrid() 
// fourth()
// fifth() 
// sixth()
// seventh()
// eighth()
// tenth()
