function first(n){
    return (n != 1) ? n * first(n - 1) : 1;
}
function second(){
    function _direct_order(k,m){
        for(var i = k;i <= m;i++){
            console.log(`direct order: ${i}`);
        }
    }
    function _reverse_order(k,m){
        for(var i = m;i >= k;i--){
            console.log(`reverse order: ${i}`);
        }
    }

    second._direct_order = _direct_order    
    second._reverse_order =  _reverse_order    
}
function thrid(a){
    return ('' + a).split('').reverse().join('')
}
function fourth(n){
    return `${n}`.match(/\d/g).reduce((sum,digit) => sum+ +digit,0)
}
    
function fifth(n){
    if (n == 0 ) return ` ` 
    return `( ${fifth(n-1)} )`

}

// console.log(first(5))
// second()
// console.log(second._direct_order(10,20))
// console.log(second._reverse_order(10,20))
// console.log(thrid(12345));
// console.log(fourth(1357));
// console.log(fifth(4));