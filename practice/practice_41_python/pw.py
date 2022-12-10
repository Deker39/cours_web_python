import random

def show(func):

    def inner(*arr):
        print(func(*arr))

    return inner

#Exercise1
@show
def sum_list(*args):
    return f'sum list: {sum(*args)}'

#Exercise2
@show
def max_value(*args):
    return f'max value: {max(*args)}'

#Exercise3
@show
def third(num1):
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

    return f'Event list: {" ".join(event_list)}, amount -> {len(event_list)}\n' \
           f'Odd list: {" ".join(odd_list)}, amount -> {len(odd_list)}\n' \
           f'Negative list: {" ".join(negative_list)}, amount -> {len(negative_list)}\n' \
           f'Positive list: {" ".join(positive_list)}, amount -> {len(positive_list)}'

#Exercise4
@show
def revers_array(array):
    return f'revers list: {array[::-1]}'

#Exercise5
@show
def find_item(array,item):
    return f'find item: True' if item in array else f'find item: False'

# #Exercise6
def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)


@show
def factorial_list(array):
    return '\n'.join([f'factorial number {i} -> {fact(i)}' for i in array])


sum_list([1,2,3,4,5])
max_value([1,2,3,4,5])
third([random.randint(-10, 10) for i in range(10)])
revers_array([1,2,3,4,5])
find_item([1,2,3,4,5],3)
factorial_list([1,2,3,4,5])