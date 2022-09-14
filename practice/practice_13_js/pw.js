function first(){
    list1 = prompt('Enter first line')
    list2 = prompt('Enter second line')
    if (list1.length > list2.length){
        console.log(1);
    }
    else if(list1.length < list2.length){
        console.log(-1);
    }
    else console.log(0);
}

function second(){
    list = prompt('Enter line')
    console.log(list[0].toUpperCase() + list.slice(1));
}

function third(){
    word = ['a','e','i','o','u']
    text = prompt('Enter line')
    count = 0
    for (let j=0;j<word.length;j++){
        text.includes(word[j]) == true? count =count + 1 :    null
        
    }
    console.log(`the number of vowels a letter in the passed string: ${count}`);
}

function fourth(){
    spam = ['100% бесплатно','увеличение продаж','только сегодня','не удаляйте','ххх']
    spamExamination = prompt('Enter line')
    for (let j=0;j<spam.length;j++){
        spamExamination.toLowerCase().includes(spam[j]) == true? console.log(true):    null
        
    }
}

function fifeth(){
    text = 'hello, world!'
    lenth = 8
    if (text.length > lenth){
        return text.slice(0,5)+'...'
    }

}

function sixth(){
    // str = 'tenet'
    str= prompt('Enter line')
    console.log( Array.prototype.reverse.call(str.split('')).join('') == str)
}

function seventh(){
    line = prompt("enter line")
    console.log(line.split(' ').length);
}

function eighth(){
    line = prompt("enter line")
    var array = line.split(' ')
    var longestWord = 0
    for(var i = 0; i < array.length; i++){
        if(array[i].length > longestWord){
        longestWord = array[i].length;
        var kek = array[i]
        }
    }
    console.log(kek);
}

function ninth(){
    line = prompt("enter line")
    var array = line.split(' ')
    var sizeWord = []
    var sum = 0
    var count = 0
    for(var i = 0; i < array.length; i++){
        sizeWord[i] = array[i].length;
    }
    for(var i = 0; i < sizeWord.length; i++){
        sum += sizeWord[i];
        count += 1

    }
    console.log(sum/count);
}

function tenth(){
    line = prompt("enter line")
    simvol = prompt("enter simvol")
    var count = 0 
    var index = []
    // console.log(line.indexOf(simvol));
    for(var i =0;i<line.length;i++){
        if(line[i]==simvol){
            index.push(i)
        }
        if (line[i].indexOf(simvol) == 0){
            count += 1
        }
        
    }
    console.log(index);
    console.log(count);

}