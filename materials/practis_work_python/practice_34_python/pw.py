# Exercise_1
def first():
    num1 = int(input('Enter start range: '))
    num2 = int(input('Enter end range: '))
    print(*range(num1, num2))
    print(f'sum: {sum(range(num1, num2))}')
    print(f'avg: {sum(range(num1, num2)) / len(range(num1, num2))}')
# Exercise_2
def second():
    def factorial(x):

        if x == 1:
            return 1
        else:
            return (x * factorial(x - 1))

    num = int(input('Enter your value: '))
    print("The factorial of", num, "is", factorial(num))

# Exercise_3
def third():
    num = int(input('Enter your value: '))
    print('Your line: ', end='')
    print('*' * num)
# Exercise_4
def fourth():
    num = int(input('Enter your value: '))
    sign = str(input('Enter your sign: '))
    print('Your line: ', end='')
    print(sign * num)

