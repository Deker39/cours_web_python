# Exercise1
def first():
    num = str(input('Enter ypur value: '))
    print(f'{num[0]}',
          f'{num[1]}', sep='\n')
# Exercise2
def second():
    num = str(input('Enter ypur value: '))
    print(f'{num[0]}',
          f'{num[1]}',
          f'{num[2]}',
          f'{int(num[0]) + int(num[1]) + int(num[2])}', sep='\n')
# Exercise3
def third():
    num1 = str(input('Enter first value: '))
    num2 = str(input('Enter second value: '))
    print(f'{num1 + num2}')
# Exercise4
def fourth():
    temper = int(input('Enter temperature in Celsius: '))
    print(f'Your temperature in Fahrenheit: {9 / 5 * temper + 32}°F')
