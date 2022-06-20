var colorReg = RegExp(/^[a-zA-Z]+$/gm)
var rgbReg  = RegExp(/(\d{1,3}),(\d{1,3}),(\d{1,3})/gm)
var rgbareg = RegExp(/(\d{1,3}),(\d{1,3}),(\d{1,3}),(1|1\.?\.0|0\.?\.\d{0,}|0)/gm )
var hexReg = RegExp(/#[0-9A-Fa-f]{6}/mg)


var mainDiv = document.getElementById('view')
var creatDiv = document.createElement('div')
var colorName = document.getElementById('colorId')
var colorType = document.getElementById('typeId')
var colorCode = document.getElementById('codeId')
console.log(colorName.textContent);