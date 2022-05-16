var car = {
    made: 'Chevrolet',
    model: 'Camaro',
    release:  1966,
    avarge_speed: 120,
    show_info: function(){
        console.log(`Made by ${this.made} \nModel: ${this.model}\nCreat in ${this.elease}\naverage speed: ${this.avarge_speed}`)
    },
    distance: function(time){
        // var time = 10
        if (Math.floor(time/4) == 0){
            chil = 0
        }else {
            chil = Math.floor(time/4)
        }
        dist = this.avarge_speed * (time+chil)
        console.log(`Distance ${dist} km`);
    }
}

console.log(car)
car.show_info()
car.distance(10)
/*--------------------------*/

var fractions = {
    numerator1: 1 ,
    denominator1: 3,
    numerator2: 2,
    denominator2: 4,
    additions: function(){
       let result_numerator = (this.numerator1*this.denominator2) + (this.numerator2*this.denominator1)
       let result_denominator = this.denominator1 * this.denominator2
       console.log(`Additions ${result_numerator}/${result_denominator}`);
    },
    subtraction: function(){
        let result_numerator = (this.numerator1*this.denominator2) - (this.numerator2*this.denominator1)
        let result_denominator = this.denominator1 * this.denominator2
        console.log(`Subtraction ${result_numerator}/${result_denominator}`);
    },
    multiplication: function(){
        let result_numerator =  this.numerator1 * this.numerator2
        let result_denominator = this.denominator1 * this.denominator2
        console.log(`Multiplication ${result_numerator}/${result_denominator}`);
    },
    division: function(){
        let result_numerator =  this.numerator1 * this.denominator2
        let result_denominator = this.denominator1 * this.numerator2
        console.log(`Division ${result_numerator}/${result_denominator}`);
    },
    cuts: function(){
    
    }
}
fractions.additions()
fractions.subtraction()
fractions.multiplication()
fractions.division()
/*--------------------------*/
var time = {
    hours: 0,
    minuts:0,
    seconds:0,
    show_time(){

    },
    time_change_seconds: function(){

    },
    time_change_minuts: function(){

    },
    time_change_hours: function(){

    }
}