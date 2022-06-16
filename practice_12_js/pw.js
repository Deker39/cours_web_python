function first(array){
    var i = 1
    array.forEach(e => {
        console.log(`Array ${i++}: ${e}`);
    });
}
function second(array){
    return  array.filter(i => i % 2 == 0)
}
function thirth(array) {
    var s = 0 
    array.forEach(e =>{
        s += e
    })
    return s  
}
function fourth(array){
    return Math.max.apply(null,array)
}
function fifth(array,index,value){
    return array[index] = value
    
}
function sixth(array,index){
    console.log(`Item deleted: ${indexDeleted+1} [${arr[indexDeleted]}]`);
    return delete array[index]
}

let arr = Array.from({length: 10}, () => Math.floor(Math.random() * 40));
let indexChanged = 5
let indexDeleted = 0
first(arr)
console.log(`Even elements in array: ${second(arr)}`);
console.log(`Sum of all array elements: ${thirth(arr)}`);
console.log(`Max element in array: ${fourth(arr)}`);
console.log(`Item changed: ${indexChanged+1} [${fifth(arr,5,34)}]`);
first(arr)
sixth(arr,indexDeleted)
first(arr)
