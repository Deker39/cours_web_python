# Exercise_1
def first():
    num1 = int(input('Enter start range: '))
    num2 = int(input('Enter end range: '))
    print('range: ', end='')
    print(*range(num1, num2))
# Exercise_2
def second():
    num1 = int(input('Enter start range: '))
    num2 = int(input('Enter end range: '))
    print('all odd numbers in the specified range: ', end='')
    print(*[i for i in range(num1, num2) if i % 2 == 1])
# Exercise_3
def third():
    num1 = int(input('Enter start range: '))
    num2 = int(input('Enter end range: '))
    print('all even numbers in the specified range: ', end='')
    print(*[i for i in range(num1, num2) if i % 2 == 0])
# Exercise_4
def fourth():
    num1 = int(input('Enter start range: '))
    num2 = int(input('Enter end range: '))
    print('range: ', end='')
    print(*range(num1, num2).__reversed__())
# Exercise_5
num1 = int(input('Enter start range: '))
num2 = int(input('Enter end range: '))
num3 = 0

if num2 <= num1:
    print(f'range bounds normalization')
    num3 = num1
    num1 = num2
    num2 = num3
    print('all even numbers in the specified range: ', end='')
    print(*[i for i in range(num1, num2) if i % 2 == 0])
else:
    print('all even numbers in the specified range: ', end='')
    print(*[i for i in range(num1, num2) if i % 2 == 0])

