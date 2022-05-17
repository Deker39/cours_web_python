let chose = +prompt('Введи номер задание 1-3')

switch (chose) {
    case 1:
        var car = {
            made: 'Chevrolet',
            model: 'Camaro',
            release:  1966,
            avarge_speed: 120
        }
        function show_info(){
            console.log(`Made by ${car.made} \nModel: ${car.model}\nCreat in ${car.release}\naverage speed: ${car.avarge_speed} km/h`)
        }
        function distance(){
            let dist = +prompt('Введи расстояние');
            let time_in_road = 0
            let time_with_out_rest = 0
            let restTime = 0
            let time = 0
            let hours = 0

            time_with_out_rest = dist / car.avarge_speed;
            time_with_out_rest = parseInt(time_with_out_rest * 10) / 10;
            if (time_with_out_rest > 4) {
                restTime = parseInt(time_with_out_rest / 4);
            }
            time_in_road = restTime + time_with_out_rest;1
            time = (time_in_road * 60)
            hours = Math.floor(time / 60 )
            time = time - (hours * 60)
            
            console.log(`Time ${hours}:${time} `);

        }
        
        console.log(car)
        show_info()
        distance() 
        break;

/*--------------------------*/

    case 2:
        var fraction = {
            numerator: 0,
            denominator: 0,
        }

        firs_fraction = Object.assign({}, fraction)
        second_fraction = Object.assign({}, fraction)
        result = Object.assign({}, fraction)

        firs_fraction.numerator = +prompt('Введи числитель первого элемента')
        firs_fraction.denominator = +prompt('Введи знаменатель первого элемента')

        second_fraction.numerator = +prompt('Введи числитель второго элемента')
        second_fraction.denominator = +prompt('Введи знаменатель второго элемента')

        console.log(`Первая дробь ${firs_fraction.numerator}/${firs_fraction.denominator}`);
        console.log(`Вторая дробь ${second_fraction.numerator}/${second_fraction.denominator}`);

        function gcd(n, m) {
            return m == 0 ? n : gcd(m, n % m);
        }

        function nok(n, m) {
            return n * m / gcd(n, m);
        }

        function multiplication(){
            result.numerator = firs_fraction.numerator * second_fraction.numerator;
            result.denominator = firs_fraction.denominator * second_fraction.denominator;
            console.log(`Multiplication = ${result.numerator}/${result.denominator}`);
        }

        function  division(){
            result.numerator = firs_fraction.numerator * second_fraction.denominator;
            result.denominator = firs_fraction.denominator * second_fraction.numerator;
            console.log(`Division  = ${result.numerator}/${result.denominator}`);
        }

        function additions(){
            let NOK = 0;

            NOK = nok(firs_fraction.denominator, second_fraction.denominator);

            let first_additions = NOK / firstFraction.denominator;
            let second_additions = NOK / secondFraction.denominator;
        }
        multiplication()
        division()


        //     additions(){
        //        let result_numerator = (this.numerator1*this.denominator2) + (this.numerator2*this.denominator1)
        //        let result_denominator = this.denominator1 * this.denominator2
        //        console.log(`Additions ${result_numerator}/${result_denominator}`);
        //     }
        //     subtraction(){
        //         let result_numerator = (this.numerator1*this.denominator2) - (this.numerator2*this.denominator1)
        //         let result_denominator = this.denominator1 * this.denominator2
        //         console.log(`Subtraction ${result_numerator}/${result_denominator}`);
        //     }
        //     multiplication(){
        //         let result_numerator =  this.numerator1 * this.numerator2
        //         let result_denominator = this.denominator1 * this.denominator2
        //         console.log(`Multiplication ${result_numerator}/${result_denominator}`);
        //     }
        //     division(){
        //         let result_numerator =  this.numerator1 * this.denominator2
        //         let result_denominator = this.denominator1 * this.numerator2
        //         console.log(`Division ${result_numerator}/${result_denominator}`);
        //     }
        //     cuts(){
        //         let m = this.numerator1
        //         let n = this.denominator1
        //         for (i = 2; i <= m;i++){
        //             if(m % i === 0 && n % i ===0){
        //                 m = m / i, n = n / i
        //             }
        //         }
        //         console.log(`Cuts ${m}/${n}`);
        //     }
        // }
        // console.log(fractions);
        // fractions.additions()
        // fractions.subtraction()
        // fractions.multiplication()
        // fractions.division()
        // fractions.cuts()
        break;

/*--------------------------*/
    
    case 3:
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
        break;
     
}





