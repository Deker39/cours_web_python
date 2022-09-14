# Exercise1
import math


def first():
    time = int(input('Enter time in seconds: '))
    if time > 86400:
        print('your value is greater than a day')
    else:
        hour = int(time / 3600)
        minut = int((time - hour * 3600) / 60)
        second = (time - hour * 3600) - minut * 60

        print(f'hour:{hour},minut:{minut},second:{second}')
        if hour == 24:
            print(f'left until midnight: 00:00:00')
        else:
            print(f'left until midnight: {23 - hour}:{60 - minut}:{60 - second}')
# Exercise2
def second():
    num = int(input('Enter circle diameter: '))
    print(f'1 - area of a circle',
          f'2 - perimeter of a circle', sep='\n')
    fun = int(input('Сhoose what to do: '))
    if fun == 1:
        print(f'S = {(math.pi * (num * num)) / 4}')
    elif fun == 2:
        print(f'P = {2 * math.pi * (num / 2)}')
    else:
        print(f'value is not correct: {fun}')
# Exercise3
def third():
    price = int(input('Enter cost of one game console: '))
    amount = int(input('Enter amount games console: '))
    discount = int(input('Enter discount percentage: '))

    print(f'Your order:',
          f'Amount games console: {amount} ',
          f'Discount percentage: {discount}%', sep='\n')
    print(f'1 - calculate total order amount',
          f'2 - the cost of one set-top box, taking into account the discount', sep='\n')
    fun = int(input('Сhoose what to do: '))
    if fun == 1:
        print(f'total order amount: {price * amount * (100 - discount) / 100} USD')
    elif fun == 2:
        print(f'the cost of one set-top box, taking into account the discount: {price * (100 - discount) / 100} USD')
    else:
        print(f'value is not correct: {fun}')
# Exercise4
def fourth():
    size = int(input('Enter file size in gigabytes: '))
    speed = int(input('Enter internet connection speed in bits per second: '))

    print(f'1 - how many hours does it take to download a file',
          f'2 - how many minutes does it take to download a file',
          f'3 - how many seconds does it take to download a file', sep='\n')
    fun = int(input('Сhoose what to do: '))
    size = (((size * 1024) * 1024) * 1024) * 8
    # print(size/speed)
    if fun == 1:
        print(f'file is downloaded via: {int(((size / speed) / 60) / 60)} hourse')
    elif fun == 2:
        print(f'file is downloaded via: {int((size / speed) / 60)} minutes')
    elif fun == 3:
        print(f'file is downloaded via: {int(size / speed)} seconds')
    else:
        print(f'value is not correct: {fun}')
# Exercise5
def fifth():
    h = int(input('Enter hour time '))
    if 0 < h < 6:
        print('Good Night')
    elif 6 <= h < 13:
        print('Good Morning')
    elif 13 <= h < 17:
        print('Good Day')
    elif 17 <= h <= 24:
        print('Good Evening')
    else:
        print("Unkown time")
