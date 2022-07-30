// ----------------------Exercise 1---------------------
class Button{
    constructor(width,heigth){
        this.width = width
        this.height = heigth
    }

    showBtn(){
        let b = document.createElement('button')

        b.style.width = `${this.width}px`
        b.style.height = `${this.height}px`

        b.classList.add('d-flex', 'justify-content-center','align-items-center')

        document.body.appendChild(b)
    }

}

class BootstrapButton extends Button{
    constructor(width,heigth,color){
        super(width,heigth)
        this.color = color
    }

    showBtn(){
        let b = document.createElement('button')

        b.style.width = `${this.width}px`
        b.style.height = `${this.height}px`
        b.style.backgroundColor = this.color

        b.classList.add('d-flex', 'justify-content-center')

        document.body.appendChild(b)
    }
}

var tit1 = document.createElement('h1')
tit1.textContent = 'Exercise 1#'
tit1.classList.add('d-flex', 'justify-content-center')
document.body.appendChild(tit1)


let b1 = new Button(100,50)
let b2 = new BootstrapButton(100,50,'red')

b1.showBtn()
b2.showBtn()


var tit2 = document.createElement('h1')
tit2.textContent = 'Exercise 2#'
tit2.classList.add('d-flex', 'justify-content-center')
document.body.appendChild(tit2)

// ----------------------Exercise 2---------------------
class DescribingFigure{
    constructor(name,side,arr){
        this.name = name
        this.side = side
        this.arr = arr

    }

    get getName(){
        return this.name
    }

    figureInformation(){
        var count = 1
        var contInfo = document.createElement('div')
        var info = document.createElement('p')
        var area = document.createElement('p')
        var perimeter = document.createElement('p')

        info.classList.add('fw-bold')
        contInfo.classList.add('border','m-4','p-2')

        info.textContent = `Figure: ${this.getName}`
        area.textContent += `area: ${this.area()}`
        perimeter.textContent += `perimeter: ${this.perimeter()} cm.`
        
        document.body.appendChild(contInfo) 
        contInfo.appendChild(info)

        for(var i =0;i<this.side;i++){
            var describ = document.createElement('p')
            describ.textContent = `side${count} - length: ${this.arr[i]} cm.`
            contInfo.appendChild(describ)
            count++
        }        

        contInfo.appendChild(area)
        contInfo.appendChild(perimeter)
    }

    area(){
        var result = 1
        for(var i =0;i<this.side;i++){
            result *= this.arr[i]
        }

        return result

    }

    perimeter(){
        var result = 0
        for(var i =0;i<this.side;i++){
            result += this.arr[i]
        }

        return result

    }
}

function Figure(name,side,length = []) {
    this.name = name;
    this.side = side;
    this.length = length;
  }

let figureObject1 = new Figure('figure1',5,[2,2])
let figureObject2 = new Figure('figure2',5,[2,2,3])
let figureObject3 = new Figure('figure3',5,[2,2,3,3])
let figureObject4 = new Figure('figure4',5,[2,2,3,3,4])
let figureObject5 = new Figure('figure5',5,[2,2,3,3,4,5])

arr1 =[figureObject1,figureObject2,figureObject3,figureObject4,figureObject5]

// let fig = new DescribingFigure(figureObject1['name'],figureObject1['side'],figureObject1['length'])
let fig = new DescribingFigure([figureObject1,figureObject2,figureObject3,figureObject4,figureObject5].forEach(e => {
    e['name'],e['side'],e['length']}))
fig.figureInformation()

class Square extends DescribingFigure{
    constructor(name,arr){
        super(name)
        this.arr = arr
    }
    figureInformation(){
        var contInfo = document.createElement('div')
        var info = document.createElement('p')
        var describ = document.createElement('p')
        var area = document.createElement('p')
        var perimeter = document.createElement('p')

        info.classList.add('fw-bold')
        contInfo.classList.add('border','m-4','p-2')

        info.textContent = `Figure: ${this.getName}`
        describ.textContent = `sides - length: ${this.arr} cm.`
        area.textContent += `area: ${this.area()}`
        perimeter.textContent += `perimeter: ${this.perimeter()} cm.`

        document.body.appendChild(contInfo)
        contInfo.appendChild(info)
        contInfo.appendChild(describ)
        contInfo.appendChild(area)
        contInfo.appendChild(perimeter)
    }

    
    area(){
        return this.arr*this.arr
    }

    perimeter(){
          return this.arr*4
    }
    
}
class Rectangle extends DescribingFigure{
    constructor(name,arr = [] ){
        super(name)
        this.arr = arr
        arr.length = 2 
    }

    figureInformation(){
        var count = 1
        var contInfo = document.createElement('div')
        var info = document.createElement('p')
        var area = document.createElement('p')
        var perimeter = document.createElement('p')

        info.classList.add('fw-bold')
        contInfo.classList.add('border','m-4','p-2')

        info.textContent = `Figure: ${this.getName}`
        area.textContent += `area: ${this.area()}`
        perimeter.textContent += `perimeter: ${this.perimeter()} cm.`
        
        document.body.appendChild(contInfo) 
        contInfo.appendChild(info)

        for(var i =0;i<this.arr.length;i++){
            var describ = document.createElement('p')
            describ.textContent = `side${count} - length: ${this.arr[i]} cm.`
            contInfo.appendChild(describ)
            count++
        }        

        contInfo.appendChild(area)
        contInfo.appendChild(perimeter)
    }

    area(){
        return this.arr[0]*this.arr[1]
    }

    perimeter(){
          return this.arr[0]*2+this.arr[1]*2
    }
    
}
class Triangle extends DescribingFigure{
    constructor(name,arr = []){
        super(name)
        this.arr = arr
        arr.length = 3
    }

    figureInformation(){
        var count = 1
        var contInfo = document.createElement('div')
        var info = document.createElement('p')
        var area = document.createElement('p')
        var perimeter = document.createElement('p')

        info.classList.add('fw-bold')
        contInfo.classList.add('border','m-4','p-2')

        info.textContent = `Figure: ${this.getName}`
        area.textContent += `area: ${this.area()}`
        perimeter.textContent += `perimeter: ${this.perimeter()} cm.`
        
        document.body.appendChild(contInfo) 
        contInfo.appendChild(info)

        for(var i =0;i<this.arr.length;i++){
            var describ = document.createElement('p')
            describ.textContent = `side${count} - length: ${this.arr[i]} cm.`
            contInfo.appendChild(describ)
            count++
        }        

        contInfo.appendChild(area)
        contInfo.appendChild(perimeter)
    }

    area(){
        var p = this.perimeter()/2
        return Math. sqrt(p*(p-this.arr[0])*(p-this.arr[1])*(p-this.arr[2]))
    }

    perimeter(){
          return this.arr[0]+this.arr[1]+this.arr[2]
    }

}

let square = new Square('square',4)
let rectangle = new Rectangle('rectangle',[1,2])
let triangle = new Triangle('triangle',[5,5,6])

square.figureInformation()
rectangle.figureInformation()
triangle.figureInformation()

// ----------------------Exercise 3---------------------