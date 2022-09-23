import  random

ls1 = [random.randint(-10,10) for i in range(0,10)]
ls2 = [random.randint(-20,10) for y in range(0,10)]
ls3 = [random.randint(0,100) for a in range(0,10)]
ls4 = [random.randint(-10,250) for b in range(0,10)]

print(f'first list: {ls1}\n'
      f'second list: {ls2}\n'
      f'third list: {ls3}\n'
      f'hourth list: {ls4}')
ls5 = []
revers_list = []
[ls5.extend(item) for item in zip(ls1,ls2,ls3,ls4)]
print(ls5)
choose_sort = int(input('1.sort ascending\n2.sort descending\nChoose: '))

if choose_sort == 1:
    ls5 = list(set(ls5))
elif choose_sort == 2:
    revers_list = list(set(ls5)).copy()
    revers_list.reverse()
    ls5 = revers_list
else:
    print('incorrect choice')
    choose_sort = input('1.sort ascending\n2.sort descending\nChoose: ')

print(f'five list: {ls5}')

choose_find = int(input('Enter your value: '))
if choose_find in ls5:
    print(f'fined: {choose_find}\n'
          f'index: {ls5.index(choose_find)}')
else: print('your value out of range')
