def show(func):

    def inner(arr):
        print(func(arr))

    return  inner

#Exercise 1
@show
def cursiv(text):
    return f'\x1B[3m{text}\x1B[3m'

#Exercise 2
@show
def diff(array):
    return f'even: {" ".join([str(i) for i in range(array[0],array[1]) if i%2 != 0])}'

#Exercise 3
def print_line(length,direction,symbol):
    if direction == 'vertical':
        for i in range(0,length):
            print(symbol)
    elif direction == 'horizontal':
        print(length*(symbol+' '))
    else:
        print('Not correct value ')

#Exercise 4
@show
def max_value(*args):
    return f'min value: {max(*args)}'

#Exercise 5
@show
def products_numbers(array):
    max = 0
    if array[0] > array[1]:  array[0],array[1] = array[1],array[0]
    for i in range(array[0], array[1] + 1):
        max += i
    return f'sum of numbers: {max}'

#Exercise 6
@show
def find_simple_numb(value):
    for i in range(2,value):
        if value % i ==0:
            return f'number simple: False'
    else: return f'number simple: True'

@show
def lucky_number(array):
    return 'lucky number' if sum([int(x) for x in str(array)][0:3]) == sum([int(x) for x in str(array)[::-1]][0:3]) else  'not lucky'





cursiv('''
“Don't let the noise of others' opinions
drown out your own inner voice.”
                            Steve Jobs
''')

diff([5,20])
print_line(5,'vertical','&')
print_line(5,'horizontal','&')
max_value([1,2,3,4,5])
products_numbers([1,5])
find_simple_numb(4)
lucky_number(123420)
