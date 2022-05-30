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

// first()
// second()
// third()
// fourth()
fifth()