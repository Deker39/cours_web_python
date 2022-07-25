# Exercise_1
def first():
    num = int(input('Enter your value: '))
    [print(f'{num} * {x} = {x * num}') for x in range(1, 11)]

# Exercise_2
def second():
    USD_buy = 35.80
    USD_sale = 36.70

    EUR_buy = 36.2
    EUR_sale = 37.3

    print('1 - Sell currency\n2 - Buy currency\n')
    answer = int(input('make choose: '))
    if answer == 1:
        answer = int(input('Witch currency you want sell?\n1.USD\n2.EUR\n'))
        if answer == 1:
            count = int(input('Enter count USD: '))
            print(f'You sell - {count} USD, get - {int(count * USD_buy)} UAH')
        elif answer == 2:
            count = int(input('Enter count EUR: '))
            print(f'You sell - {count} EUR, get - {int(count * EUR_buy)} UAH')

    elif answer == 2:
        answer = int(input('Witch currency you want buy?\n1.USD\n2.EUR'))
        if answer == 1:
            count = int(input('Enter count UAH: '))
            print(f'You sell - {count} UAH, get - {int(count / USD_sale)} USD')
        elif answer == 2:
            count = int(input('Enter count UAH: '))
            print(f'You sell - {count} UAH, get - {int(count / EUR_sale)} EUR')

# Exercise_3
def third():
    range_start = int(input('Enter start range: '))
    range_end = int(input('Enter end range: '))
    num1 = int(input('Enter your value: '))

    while (range_start <= num1 <= range_end) == False:
        num1 = int(input('Enter your value: '))

    print(*[f'!{x}!' if x == num1 else x for x in range(range_start, range_end + 1)])

# Exercise_4
def fourth():
    from random import randint

    num = -1
    r = randint(1, 500)
    count = 0

    while num != 0:
        try:
            num = int(input('Enter guess: '))
            if num < r:
                print('my nuber more than your...')
            elif num > r:
                print('my number so less...')
            elif num == r:
                print(f'You rigth: {num}')
                break
        except:
            print('unkomon nubmer!')
        count += 1
    print(f'you try: {count}')