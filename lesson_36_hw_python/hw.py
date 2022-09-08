import random

def show(func):
    def inner(arr):
        func(arr)
        for i in range(0, len(arr)):
            print(f'{i + 1}', end='\t')
            for i2 in range(0, len(arr[i])):
                print(f'{arr[i][i2]}', end='\t')
            print()
    return  inner

@show
def sort_indef(arr):
    print('Array sorted indef')
    arr.sort(key=lambda x: x[0])

@show
def sort_tel(arr):
    print('Array sorted tel')
    arr.sort(key=lambda x: x[1])

@show
def normal(arr):
    print('Array normal')


indef_code = [random.randint(1000,9999) for i in range(0,10)]
tel = ['+380' + str(random.randint(550000000,999999999)) for i in range(0,10)]

mixed = [[i,j] for i,j in zip(indef_code,tel)]

print('please make a choose\n'
      '1.Sort by identification codes\n'
      '2.Sort by phone numbers\n'
      '3.Display a list of users with codes and phones\n'
      '4.Exit')
choose = int(input('Choose: '))

while choose != 4:
    if choose == 1:
        sort_indef(mixed)
        choose = int(input('Choose: '))
    elif choose == 2:
        sort_tel(mixed)
        choose = int(input('Choose: '))
    elif choose == 3:
        normal(mixed)
        choose = int(input('Choose: '))
else:
    print('Exit')
