function first(){
    let first = prompt('Enter first value')
    let second = prompt('Enter first value')
    console.log(`Min value: ${Math.min(first,second)}`);
}
function second(){
    let value = prompt('Enter value')
    let degree = prompt('Enter degree value')
    console.log(`Your value with degree: ${Math.pow(value,degree)}`);
}
function thrid(){
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
function fourth(){
    let num = prompt('Enter your value')

    let flag = true;
    for (let i = 2; i < num; i++) {
        if (num % i == 0) {
            flag = false;
            alert(`your value is not simple: ${num}`)
            break; 
        }        
    }
    alert(`your value is simple: ${num}`)
}
function fifth(){
   let multi = prompt('Enter your value')
   for(var i = 1; i <= 10;i++){
       console.log(`${i}*${multi}=${multi*i}`);
   }
}
function sixth(){
    let n1 = Number(prompt('Enter your value'))
    let n2 = Number(prompt('Enter your divider value'))
    let n 
    let result 
    if (n1 > n2){
        n = Math.floor(n1/n2)
        result = n1 - (n2*n)
        console.log(result);
    }else{
        console.log(n1);
    }
}

function forNubers(){
    let i = []
    i = prompt('Enter number through whom')
    i = i.split(',')
    return i 
}

function seventh(){
    let res = 0
    let i = forNubers()
    for (j = 0; j < i.length;j++){     
        res = res + eval(i[j])    
    }
    console.log(res);
}
function eighth(){
    let i = forNubers()
    console.log( Math.max.apply(null, i));
}
function nineth(){
    let start = Number(prompt('Enter start of range'))
    let end = Number(prompt('Enter end of range'))
    let flag = prompt('Enter true – четные or false – нечетные')
    for (var i = start; i <= end;i++){
        if (flag == 'true'){
            if (i % 2 == 0) {
                console.log(i);
              }
        }if(flag == 'false'){
            if (i % 2 != 0) {
                console.log(i);
              }
        }
        
    }
}
function tenth(){
    let date = prompt('Example: 1998.09.26\nEntar date:')
    const options = { month: 'long'};
    date = new Date(date)
    let next_day = date.getDate()+1
    let month = new Intl.DateTimeFormat('en-US', options).format(date)
    console.log(`Next day : ${next_day} ${month}`);
}

// first()
// second()
// thrid()
// fifth()
// sixth()
// seventh()
// eighth()
// nineth()
// tenth()