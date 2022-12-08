import math
import random

negative_numbers = []
even_numbers = []
odd_numbers = []
multiple_of_three = []

def choose(item):
    if item % 2 == 0:
        even_numbers.append(item)
    elif item % 2 != 0:
        odd_numbers.append(item)
        if item % 3 == 0:
            multiple_of_three.append(item)

# Exercise1
def first():
    num1 = [random.randint(-10, 10) for i in range(10)]

    for i in num1:
        if i < 0 :
            negative_numbers.append(i)
            choose(i)
        else:
            choose(i)

    print(*num1)
    print(f'negative numbers: {sum(negative_numbers)}')
    print(f'even numbers: {sum(even_numbers)}')
    print(f'odd numbers: {sum(odd_numbers)}')
    print(f'multiple of three: {math.prod(multiple_of_three)}')
    print(f'range betwen min <{min(num1)}> and max <{max(num1)}>: {math.prod(num1[min(num1):max(num1)])}')

# Exercise2
def second():
    num1 = [random.randint(-10, 10) for i in range(10)]
    event_list = []
    odd_list = []
    negative_list = []
    positive_list = []


    for i in num1:
        if i > 0:
            positive_list.append(str(i))
            if i % 2 == 0:
                event_list.append(str(i))
            else:
                odd_list.append(str(i))
        else:
            negative_list.append(str(i))
            if i % 2 == 0:
                event_list.append(str(i))
            else:
                odd_list.append(str(i))

    print(f'Event list: {" ".join(event_list)}')
    print(f'Odd list: {" ".join(odd_list)}')
    print(f'Negative list: {" ".join(negative_list)}')
    print(f'Positive list: {" ".join(positive_list)}')

# first()
second()