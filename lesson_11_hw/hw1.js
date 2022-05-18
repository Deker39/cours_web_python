class Circle{

    #radius
    constructor(radius){
        this.#radius = radius
    }
    square_circle(){
        var square = Math.PI * this.radius**2
        console.log(`Radius: ${Math.floor(square)}`);
    }
    length_circle(){
        var length = Math.PI * this.diametr
        console.log(`Lenght: ${Math.floor(length)}`);
    }
    get radius(){
        return this.#radius
    }
    set radius(radius){
        this.#radius = radius
    }
    get diametr(){
        return this.#radius*2
    }

}

let kek  = new Circle(4)
kek.square_circle()
kek.length_circle()