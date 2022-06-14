function first(obj){
    return`Point Up: (${obj.leftUperPointX},${obj.leftUperPointY})\nPoint Up: (${obj.rigthBotPointX},${obj.rigthBotPointY})`
}
function second(obj){
    return obj.rigthBotPointX-obj.leftUperPointX
}
function  thrid(obj){
    return obj.leftUperPointY-obj.rigthBotPointY
}
function fourth(obj){
    return second(obj)*thrid(obj)
}
function  fifth(obj){
    return 2*(second(obj)+thrid(obj))
}
function  sixth(obj,value){
    return second(obj) + value
}
function  seventh(obj,value){
    return thrid(obj) + value
}
function  eighth(obj,valueX,valueY){
    return [second(obj) + valueX,thrid(obj) + valueY]

}
function  nineth(obj,value){
    return [obj.leftUperPointX + value,obj.rigthBotPointX + value]

}
function  tenth(obj,value){
    return [obj.leftUperPointY + value,obj.rigthBotPointY + value]
}
function eleventh(obj,valueX,valueY){
    return [obj.leftUperPointX + valueX,obj.rigthBotPointX + valueX,obj.leftUperPointY + valueY,obj.rigthBotPointY + valueY]
}
function twelfth(obj,valueX,valueY){
    console.log(fourth(obj)); 
    
}

let rectangle = {
    leftUperPointX: 5,
    leftUperPointY: 12,
    rigthBotPointX : 10,
    rigthBotPointY : 3
}
let randX = Math.floor(Math.random() * 10 )
let randY = Math.floor(Math.random() * 10 )

let randPointX = Math.floor(Math.random() * 10 )
let randPointY = Math.floor(Math.random() * 10 )

// rectangle['leftBotPointX'] = rectangle.leftUperPointX
// rectangle['leftBotPointY'] = rectangle.rigthBotPointY
// rectangle['rigthUperPointX'] = rectangle.rigthBotPointX
// rectangle['rigthUperPointY'] = rectangle.leftUperPointY

console.log(rectangle);
console.log(`Random numbers for X: ${randX}\nRandom numbers for Y: ${randY}`);
console.log(first(rectangle));
console.log(`Wight: ${second(rectangle)} cm.`);
console.log(`Hight: ${thrid(rectangle)} cm.`);
console.log(`Area of a rectangle: ${fourth(rectangle)}`);
console.log(`Rectangle perimeter: ${fifth(rectangle)}`);
console.log(`New wight: ${sixth(rectangle,randX)} cm.`);
console.log(`New hight: ${seventh(rectangle,randY)} cm.`);
console.log(`New wigth and hight a recetangle: ${eighth(rectangle,randX,randY)}`);
let nine = nineth(rectangle,randX)
let ten =  tenth(rectangle,randY)
let eleven = eleventh(rectangle,randX,randY)
console.log(`New x-coordinates: (${nine[0]},${rectangle.leftUperPointY}),(${nine[1]},${rectangle.rigthBotPointY})`);
console.log(`New y-coordinates: (${rectangle.leftUperPointX},${ten[0]}),(${rectangle.rigthBotPointX},${ten[1]})`);
console.log(`New coordinates: (${eleven[0]},${eleven[2]}),(${eleven[1]},${eleven[3]})`);
console.log(twelfth(rectangle,randPointX,randPointY));
