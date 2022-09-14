function first(){
    let sim = prompt('Enter number simbol')
    let i = 0 
    let list = ''
    while (i<sim) {
        list = list + '#'
        document.write(list)
        i++
    }
}
function second(){
    let val = prompt('Enter number simbol')
    let i = 0
    let list = ''
    while (val >= 0 ) {
        let list = '' + val
        document.write(list)
        val--
    }
}
function third(){
    let val = Number(prompt('Enter number simbol'))
    let degree = prompt('Enter number degree')
    let i = 1
    let res = val
    while (i<degree) {
        res *=val    
        i++   
    }
    document.write(res)
}
function fourth(){
    let numb1 = prompt('Enter first number');
    let numb2 = prompt('Enter second number');
    let numb3;
    while(numb1 != numb2){
        if(numb1 > numb2) {
            numb1= numb1 -numb2
        } 
        else if(numb1 < numb2){
            numb3 = numb1
            numb1 = numb2
            numb2 = numb3
        }
        numb3 = numb1
    }
    document.write(numb3);
}
function fifth(){
    let n = prompt('Enter number');
    let result = 1 
    let i = n
    while(i>1){
        result *= i;
        i--
    }
    document.write(result)
}
function sixth(){
    let ans
    do {
        ans = prompt('Solve the equation 2+2*2 \nyour answer')
    } while (ans != 6);
    alert('that\'s the right decision 2 + 2 * 2 = 6')
}
function seventh(){
    let d 
    let c = 0 
    let a = 1000
    do {
        d = a / 2
        a = d
        c++
    } while (a > 50);
    alert(`value: ${a}, amount: ${c}`)
}
function eighth(){
   let a = prompt('Enter your value')

    for (let i = 1; i <= 100; i++) {
        if(i%a == 0){
            document.write(`${i} \n`);
        }
    }

}
function ninth(){
    let a = prompt('Enter your min-value')
    let b = prompt('Enter your max-value')
    let c = 0
    for (a; a <= b; a++) {
       if(c == 4){
        document.write(`${a} \n`);
        c=0
       }
       c++
    }
}
function tenth(){
    let num = prompt('Enter your value')

    let flag = true;
    for (let i = 2; i < num; i++) {
        if (num % i == 0) {
            flag = false;
            alert(`your value is not simple: ${num}`)
            return 
        }        
    }
    alert(`your value is simple: ${num}`)
}
// first()
// second()
// third()
// fourth()
// fifth()
// sixth()
// seventh()
// eighth()
// ninth()
// tenth()