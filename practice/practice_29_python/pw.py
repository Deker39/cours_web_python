# Exercise1
def first():
    num = int(input('Enter your value: '))
    if num % 2 == 0:
        print(f'Even nubmer: {num}')
    else:
        print(f'Odd nubmer: {num}')
# Exercise2
def second():
    num = int(input('Enter your value: '))
    if num % 7 == 0:
        print(f'Nubmer {num} is multiple 7')
    else:
        print(f'Nubmer {num} is not multiple 7')
# Exercise3
def third():
    num1 = int(input('Enter first value: '))
    num2 = int(input('Enter second value: '))
    if num1 > num2:
        print(f'Max:{num1}')
    elif num1 == num2:
        print(f'they are equal: {num1} = {num2}')
    else:
        print(f'Max:{num2}')
# Exercise4
def fourth():
    num1 = int(input('Enter first value: '))
    num2 = int(input('Enter second value: '))
    if num1 < num2:
        print(f'Min:{num1}')
    elif num1 == num2:
        print(f'they are equal: {num1} = {num2}')
    else:
        print(f'Min:{num2}')
# Exercise5
num1 = int(input('Enter first value: '))
num2 = int(input('Enter second value: '))
print(f'1 - sum of two numbers',
      f'2 - the difference between two numbers',
      f'3 - arithmetic mean of two numbers',
      f'4 - product of two numbers',sep='\n')
fun =  int(input('enter number what to do: '))
if fun == 1:
    print(f'sum of two numbers: {num1+num2}')
elif fun == 2:
    print(f'the difference between two number: {num1-num2}')
elif fun == 3:
    print(f'arithmetic mean of two numbers: {(num1 + num2)/2}')
elif fun == 4:
    print(f'product of two numbers: {num1 * num2}')
else:
    print(f'Your enter incorrect value: {fun}')