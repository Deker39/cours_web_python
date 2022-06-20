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
/*-------------------------------------*/   

function seventh(arr1,arr2) {
    arr_jointed = arr1.concat(arr2)
    return arr_jointed = arr_jointed.filter(function(item,pos) {return arr_jointed.indexOf(item) == pos}) 
    // return [...new Set([...arr1 ,...arr2])]
}
function eighth(arr1,arr2){
    var a_values = Object.keys(arr1).map(function(key){
        return arr1[key];
    });
    
    var b_values = Object.keys(arr2).map(function(key){
        return arr2[key];
    });
    for (var a_key in a_values) {
        if (b_values.indexOf(a_values[a_key]) != -1) {
           arr_repetition.push(a_values[a_key])
        }
    }
    return arr_repetition
  
   
}
function nineth(arr1,arr2){
    var a_values = Object.keys(arr1).map(function(key){
        return arr1[key];
    });
    
    var b_values = Object.keys(arr2).map(function(key){
        return arr2[key];
    });

    for (var a_key in a_values) {
        if (b_values.indexOf(a_values[a_key]) == -1) {
            arr_remove.push(a_values[a_key])
        }
    }
    return arr_remove
}

let arr_jointed = []
let arr_remove = []
let arr_repetition = []
let arr_one = Array.from({length: 5}, () => Math.floor(Math.random() * 40));
let arr_two = Array.from({length: 5}, () => Math.floor(Math.random() * 40));
console.log(arr_one);
console.log(arr_two);
console.log(`All elements from two arrays without repetition ${seventh(arr_one,arr_two)}`);
console.log(`Common elements without repetition: ${eighth(arr_one,arr_two)}`);
console.log(`All elements from the first array, which are not in the second array: ${nineth(arr_one,arr_two)}`);
/*-------------------------------------*/ 

var fruit = ['apricot', 'quince', 'orange', 'watermelon', 'banana', 'grape', 'pomegranate', 'grapefruit', 'pear', 'guava', 
            'melon', 'fig', 'cantaloupe','apple', 'carambola', 'kiwi', 'lemon', 'mango', 'marania', 'medlar', 'pepino', 'peach', 
            'pitaya', 'pomelo', 'physalis', 'persimmon']

let cont = document.createElement('section')
let ul = document.createElement('ul')

document.body.appendChild(cont)
cont.appendChild(ul)

cont.classList.add('container')
ul.classList.add('list-group','list-group-flush')

for( var i = 0; i< fruit.length;i++){
    var li = document.createElement('li')
    ul.appendChild(li)
    li.classList.add('list-group-item')
    li.innerHTML = li.innerHTML + fruit.sort()[i]
}

function tenth(nameFruit){
    alert(`Index of your fruit: ${fruit.indexOf(nameFruit)}`)
    return fruit.indexOf(nameFruit)
}

ul.addEventListener('click', function(e){
    e.target.classList.toggle('bg-danger')
    console.log(`Index of your fruit: ${fruit.indexOf(e.target.textContent)}`);
    
})
ul.addEventListener('mouseout',function(e) {
    e.target.classList.remove('bg-danger')
})

