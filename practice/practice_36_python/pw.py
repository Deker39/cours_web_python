# Exercise_1
def first():
    zero = '0'
    num1 = str(input('Enter your value: '))
    print('1.Number of digits\n2.Sum\n3.Avg\n4.Amount zero')
    choice = int(input('Please make a choice: '))
    if choice == 1:
        print(f'number of digits: {len(num1)}')
    elif choice == 2:
        print(f'sum: {sum([int(x) for x in num1])}')
    elif choice == 3:
        print(f'avg: {sum([int(x) for x in num1]) / len(num1)}')
    elif choice == 4:
        print(f'amount zero: {len([x for x in num1 if x == zero])}')
    else:
        print(f'Not right a choice!')

# Exercise_2
def second():
    num = int(input('Enter size: '))
    for x in range(1, 4):
        for j in range(1, 5):
            print('*' * num + '_' * num, end='')
        print('\n')
    for x in range(1, 4):
        for j in range(1, 5):
            print('_' * num + '*' * num, end='')
        print('\n')

# Exercise_3
def third():
    import random

    grade = 0
    i = 0
    while i < 13:
        print('1.Simple level\n2.Medium  level\n3.Difficulty  level\n0.Exit')
        level = int(input('Enter difficulty level: '))
        if level == 1:
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
            print(f'{num1}*{num2}')
            result = int(input('Write an answer: '))
            if result == num1 * num2:
                print('Right')
                grade += 1
            else:
                print('Not right')
                grade -= 1
        elif level == 2:
            num1 = random.randint(0, 50)
            num2 = random.randint(0, 50)
            print(f'{num1}*{num2}')
            result = int(input('Write an answer: '))
            if result == num1 * num2:
                print('Right')
                grade += 2
            else:
                print('Not right')
                grade -= 2
        elif level == 3:
            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
            print(f'{num1}*{num2}')
            result = int(input('Write an answer: '))
            if result == num1 * num2:
                print('Right')
                grade += 3
            else:
                print('Not right')
                grade -= 3
        elif level == 0:
            i = 12
        else:
            print('Not right a choice!')
        i += 1
        print(f'Your grade: {grade}')


# Exercise_4
def fourth():
    i = 1
    count = 5
    while i < 6:
        print('  ' * int(count / 2) + '* ' * i + '  ' * int(count / 2))
        count -= 2
        i += 2
    i = 5
    count = 0
    while i > 0:
        print('  ' * count + '* ' * i + '  ' * count)
        count += 1
        i -= 2
    print()