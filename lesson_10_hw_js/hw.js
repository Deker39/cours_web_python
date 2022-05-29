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

        function gcd(n, m) {
            return m == 0 ? n : gcd(m, n % m);
        }

        function nok(n, m) {
            return n * m / gcd(n, m);
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



        function multiplication(){
            result.numerator = firs_fraction.numerator * second_fraction.numerator;
            result.denominator = firs_fraction.denominator * second_fraction.denominator;
            console.log(`Multiplication = ${cuts(result.numerator,result.denominator)}`);
        }

        function  division(){
            result.numerator = firs_fraction.numerator * second_fraction.denominator;
            result.denominator = firs_fraction.denominator * second_fraction.numerator;
            console.log(`Division  = ${cuts(result.numerator,result.denominator)}`);
        }

        function additions(){
            let NOK = 0;

            NOK = nok(firs_fraction.denominator, second_fraction.denominator);

            let first_additions = NOK / firs_fraction.denominator;
            let second_additions = NOK / second_fraction.denominator;

            if (firs_fraction.denominator === second_fraction.denominator ) {

                result.numerator = firs_fraction.numerator + second_fraction.numerator;
                result.denominator = firs_fraction.denominator;

            } else if ((firs_fraction.denominator < second_fraction.denominator ) || (firs_fraction.denominator > second_fraction.denominator )) {

                result.numerator = (firs_fraction.numerator * first_additions) + (second_fraction.numerator * second_additions);
                result.denominator = NOK;

            } else {
                document.write('You entered null or something else for denominator.')
            }
            console.log(`Additions  = ${cuts(result.numerator,result.denominator)}`);
        }
        function  subtraction(){
            let NOK = 0;

            NOK = nok(firs_fraction.denominator, second_fraction.denominator);

            let first_additions = NOK / firs_fraction.denominator;
            let second_additions = NOK / second_fraction.denominator;

            if (firs_fraction.denominator === second_fraction.denominator ) {

                result.numerator = firs_fraction.numerator - second_fraction.numerator;
                result.denominator = firs_fraction.denominator;

            } else if ((firs_fraction.denominator < second_fraction.denominator ) || (firs_fraction.denominator > second_fraction.denominator )) {

                result.numerator = (firs_fraction.numerator * first_additions) - (second_fraction.numerator * second_additions);
                result.denominator = NOK;

            } else {
                document.write('неправильное значение')
            }
            console.log(`Subtraction  = ${cuts(result.numerator,result.denominator)}`);
        }
        function  cuts(m, n){
            let M = m;
            let N = n;

            for (let i = 2; i <= m; i++) {
                if (m % i === 0 && n % i === 0) {
                    M = m / i, N = n / i ;
                }
            }

            return [M, N].join('/');
        
        }
        multiplication()
        division()
        additions()
        subtraction()
        break;

/*--------------------------*/
    
    case 3:
        var time = {
            hours: 0,
            minuts:0,
            seconds:0
        }
        entered_time = Object.assign({}, time)
        let add_seconds = 0
        let add_minutes = 0
        let add_hours = 0

        entered_time.hours = +prompt('Введи часы');
        entered_time.minutes = +prompt('Введи минуты');
        entered_time.seconds = +prompt('Введи секунды');

        function show_time(){
            console.log(`Время ${entered_time.hours}:${entered_time.minutes}:${ entered_time.seconds}`);
            }
        function time_change_seconds(){
            add_seconds = +prompt('Введи секунды которые хочешь добавить(от 0 до 60)');
            if(add_seconds >= 0 && add_seconds <=60){
                entered_time.seconds += add_seconds
                if(entered_time.seconds >= 60){
                    entered_time.seconds = entered_time.seconds - 60
                    entered_time.minutes +=1
                    // console.log(`Время ${entered_time.hours}:${entered_time.minutes}:${ entered_time.seconds}`);
                }
                else{}
            }else{
                show_time()
            }
            console.log(`Время ${entered_time.hours}:${entered_time.minutes}:${ entered_time.seconds}`);
            }
        function time_change_minuts(){
            add__minuts = +prompt('Введи минуты которые хочешь добавить(от 0 до 60)');
            if(add__minuts >= 0 && add__minuts <=60){
                entered_time.minutes += add__minuts
                if(entered_time.minutes >= 60){
                    entered_time.minutes = entered_time.minutes - 60
                    entered_time.hours +=1
                    // console.log(`Время ${entered_time.hours}:${entered_time.minutes}:${ entered_time.seconds}`);
                }
                else{}
            }else{
                show_time()
            }
            console.log(`Время ${entered_time.hours}:${entered_time.minutes}:${ entered_time.seconds}`);
            }
        function time_change_hours(){
            add_hours = +prompt('Введи часы которые хочешь добавить(от 0 до 60)');
            if(add_hours >= 0 && add_hours <=60){
                entered_time.hours += add_hours
            }else{
                show_time()
            }
            console.log(`Время ${entered_time.hours}:${entered_time.minutes}:${ entered_time.seconds}`);
            }
        
        show_time()
        time_change_seconds()
        time_change_minuts()
        time_change_hours()
        break;
     
}





