#/--------------------LESSON1--------------------/
# # exercise_1
# def first():
#     print(input('Enter value first: ') +
#           input('Enter value second: ') +
#           input('Enter value third: '))
# # exercise_2
#
# def second():
#     num = int(input('Enter your number:'))
#     num1 = num // 1000
#     num2 = (num // 100) % 10
#     num3 = (num // 10) % 10
#     num4 = num % 10
#
#     return num1,num2,num3,num4
#     # print(num1 * num2 * num3 * num4)
#
# # exercise_3
#
# def third():
#     metr = int(input('Enter value metters:'))
#     cm = metr * 100
#     dm = metr * 10
#     mm = metr * 100
#     ml = metr * 1609
#     print(f'centimeters to meters: {cm}cm\n'
#           f'decimeters to meters: {dm}dm\n'
#           f'millimeters to meters: {mm}mm\n'
#           f'miles per meter: {ml}ml\n')
#
# # exercise_4
# def fourth():
#     main = int(input('Enter main triangle: '))
#     hight = int(input('Enter hight triangle: '))
#     print(f'S = {1 / 2 * main * hight} (m\u00B2)')
#
# # exercise_1
# first()
# # exercise_2
# sec = second()
# print(sec[0] * sec[1] * sec[2] * sec[3])
# # exercise_3
# third()
# # exercise_4
# fourth()
# # exercise_5
# fif = second()
# print(f'{sec[3]}{sec[2]}{sec[1]}{sec[0]}')


#/--------------------LESSON2--------------------/
#
# print(type(5))
# print(ord('A'))
#
# age = 5
# if age > 0:
#     print('hello')
#     if age == 5:
#         print('hello2')
#
#
# num = 5
# if num < 0:
#     print('Yes')
# elif num == 5:
#     print('elif')
# else:
#     print('No')

# h = int(input('Enter hour time '))
# if 0 < h < 6:
#     print('Good Night')
# elif 6 <= h <13:
#     print('Good Morning')
# elif 13 <= h < 17:
#     print('Good Day')
# elif 17 <= h <= 24:
#     print('Good Evening')
# else: print("Unkown time")

# # exercise_1
# def first():
#     num = input("Enter a six-digit number: ")
#     if not num or len(num) != 6:
#         print('error')
#     elif (int(num[0]) + int(num[1]) + int(num[2])) == (int(num[3]) + int(num[4]) + int(num[5])):
#         print('Enter a six-digit number')
#     else:
#         print('you have an unlucky number')
# # exercise_2
# def second():
#     num = input("Enter a six-digit number: ")
#     if not num or len(num) != 6:
#         print('error')
#     else: print(f'{num[5]}{num[4]}{num[2]}{num[3]}{num[1]}{num[0]}')
# # exercise_3
# def third():
#     month = int(input('Enter value a month: '))
#     if 1 <= month <= 2 or month == 12: print('Winter')
#     elif 3 <= month <= 5: print('Spring')
#     elif 6 <= month <= 8: print('Summer')
#     elif 9 <= month <= 11:print('Autumn')
#     else: print('error')
# Пользователь вводит число от 1 до 9999 (Баланс). Необходимо создать меню с которым пользователь может взаимодействовать,
# вывести в консоль меню с товарами (виды кофе) и указать ихнюю цену. Пользователь покупает выбранный кофе цена должна отниматься
# от баланса, обязательно создать проверки на нулевой баланс/большую цену та др. В конце нужно указать что купил пользователь и
# словами указать сумму с правильным окончанием. Например: Ви купили Лате, ваша сдача: 7431 – семь тысяч четыреста тридцать один
# доллар, или 2149 – две тысячи сто сорок девять долларов, 15 – пятнадцать долларов, 3 – три доллара
#
# num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
#             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
#             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
#             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
# num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
#
# def number(bal):
#     if 1 <= bal < 19:
#         return num2words1[bal]
#     elif 20 <= bal <= 99:
#         tens = bal//10
#         below_ten = bal%10
#         if below_ten == 0:
#             return num2words2[tens-2]
#         else: return num2words2[tens-2] + '-' + num2words1[below_ten]
#     else:
#         print("Number out of range")
#
#
#
# balans = input("Enter your balans: ")  # баланс от 0 до 100
# print(f'Your balanse:{balans}$, please make a choice')
# print(f'Num 1: Americano - 10$\n'
#       f'Num 2: Americano with milk - 12$\n'
#       f'Num 3: Latte - 15$\n'
#       f'Num 4: Cappuccino -20$\n'
#       f'Num 5: Espresso- 6%\n')
#
# choice = int(input("Choice: "))
#
# if not choice or len(balans) > 3 or 1 <= choice >6: print('You don\'t make a choice')
# else:
#     if int(balans) > choice:
#          if choice == 1: print(f'your order: Americano\nyour change: {int(balans) -10}-{number(int(balans) -10)}')
#          elif choice == 2: print(f'your order:Americano with milk\nyour change: {int(balans) -12}-{number(int(balans) -12)}')
#          elif choice == 3: print(f'your order: Latte\nyour change: {int(balans) -15}-{number(int(balans) -15)}')
#          elif choice == 4: print(f'your order: Cappuccino\nyour change: {int(balans) -20}-{number(int(balans) -20)}')
#          elif choice == 5: print(f'your order: Espresso\nyour chang: {int(balans) - 6}-{number(int(balans) - 6)}')
#     else: print('you poor')


#/--------------------LESSON3--------------------/
# fact = 1
# num = 5
# i = 1
# while i <= num:
#     print(f'Iteration #{i}, fact: {fact}')
#     fact *= i
#     i += 1
#
# print(fact)

# while True:
#     answer = input('Enter 0 to stop: ')
#     if answer == '0':
#         break


# num = 0
# max = 0
# min = 0
# sum = 0
# count = 0
# while True:
#
#     num = int(input('Enter num '))
#     if num == 7: break
#
#     if min > num or count == 0:
#         min = num
#     if max < num: max=num
#     sum += num
#     count +=1
#
# print(f'Sum: {sum}\nMax: {max}\nMin: {min}')
# print('bye')

# num = int(input('Enter size: '))
# for x in range(1,4):
#         for j in range(1, 5):
#                 print('*'*num + '_'*num,end='')
#         print('\n')
# for x in range(1, 4):
#         for j in range(1, 5):
#                 print('_' * num + '*' * num, end='')
#         print('\n')
#/--------------------LESSON4--------------------/

# Exception
# try:
#     number1 =  int(input("Enter number "))
#     number2 = int(input("Enter number "))
#     if number1 < 0 or number2 < 0:
#         raise ValueError('your value less 0')
# except ZeroDivisionError as f:
#     print("Base Error ")
# except ValueError as f:
#     print("Error ", str(f))
# finally:
#     print('Finaly block')

# sum = 0
# num = -1
# while num !=0:
#     try:
#         num =  int(input("Enter number, or enter 0 to exit: "))
#         sum += num
#     except (TypeError,ValueError) as f:
#         print(f'Enter please number! - {str(f)}')
#     except Exception as e:
#         print(e)
# print(f'Sum: {sum}')


# from random import randint
#
# num = -1
# r = randint(1, 500)
# count = 0
#
# while num !=0:
#     try:
#         num = int(input('Enter guess: '))
#         if num < r:
#             print('my nuber more than your...')
#         elif num > r:
#             print('mu number so less...')
#         elif num == r:
#             print(f'You rigth: {num}')
#             break
#     except:
#         print('unkomon nubmer!')
#     count += 1
# print(f'you try: {count}')


# USD_buy = 35.80
# USD_sale = 36.70
#
#
# EUR_buy = 36.2
# EUR_sale = 37.3
# print('1 - Sell currency\n2 - Buy currency\n')
# answer = int(input('make choose: '))
# if answer == 1:
#     answer = int(input('Witch currency you want sell?\n1.USD\n2.EUR\n'))
#     if answer == 1:
#         count  = int(input('Enter count USD: '))
#         print(f'You sell - {count} USD, get - {int(count*USD_buy)} UAH')
#     elif answer == 2:
#         count  = int(input('Enter count EUR: '))
#         print(f'You sell - {count} EUR, get - {int(count*USD_buy)} UAH')
#
# elif answer == 2:
#     answer = int(input('Witch currency you want buy?\n1.USD\n2.EUR'))
#     if answer == 1:
#         count  = int(input('Enter count UAH: '))
#         print(f'You sell - {count} UAH, get - {int(count/USD_sale)} USD')
#     elif answer == 2:
#         count  = int(input('Enter count UAH: '))
#         print(f'You sell - {count} UAH, get - {int(count/EUR_sale)} EUR')

#
# # а
# i = 5
# count = 0
# while i > 0:
#     print('  '*count+'* '*i)
#     count +=1
#     i -= 1
# # б
# i = 0
# count = 5
# while i < 5:
#     print('* '*i+' '*count)
#     count -=1
#     i += 1
# print()
# # в
# i = 5
# count = 0
# while i > 0:
#     print('  '*count+'* '*i+'  '*count)
#     count +=1
#     i -= 2
# print()
# # г
# i = 1
# count = 5
# while i < 6:
#     print('  '*int(count/2)+'* '*i+'  '*int(count/2))
#     count -=2
#     i += 2
# print()
# # д
# i = 5
# count = 0
# while i > 0:
#     print('  '*count+'* '*i+'  '*count)
#     count +=1
#     i -= 2
# j = 1
# count = 5
# while j < 6:
#     print('  '*int(count/2)+'* '*j+'  '*int(count/2))
#     count -=2
#     j += 2
# # е
# i = 7
# count = 0
# while i > 0:
#     print('* '*count+'  '*i+'* '*count)
#     count +=1
#     i -= 2
# j = 1
# count = 7
# while j < 6:
#     print('* '*int(count/2)+'  '*j+'* '*int(count/2))
#     count -=2
#     j += 2
# print()
# # ж
# i = 5
# count = 0
# while i > 0:
#     print('* '*count+'  '*i)
#     count +=1
#     i -= 1
# j=5
# count = 0
# while j > 0:
#     print('* '*j+'  '*count)
#     count +=1
#     j -= 1
# # з
# i = 5
# count = 0
# while i > 0:
#     print('  '*i+'* '*count)
#     count +=1
#     i -= 1
# j=5
# count = 0
# while j > 0:
#     print('  '*count+'* '*j)
#     count +=1
#     j -= 1
# print()
# # и
# i = 5
# count = 0
# while i > 0:
#     print('* '*i+'  '*count)
#     count +=1
#     i -= 1
# print('')
# # к
# i = 5
# count = 0
# while i > 0:
#     print('  '*count+'* '*i)
#     count +=1
#     i -= 1
#/--------------------LESSON5--------------------/

# name = 'Alex'
#
# print(name[0])
# print(f'{name}')
#
# line = 'Lorem ipsum con com led {0} and {1}'
# # print(line[::-1])
# print('con' in line)
#
# print(line.count('o'))
# print(line.index('o'))
# print(line.title())
# print(line.isalpha())
# print(line.find('led'))
# print(line.lower())
# print(line.capitalize())
# print(line.format('den','tom'))
# print(line.replace('o','p'))
#
# print(line.split(' '))
# print('##'.join(line.split(' ')))

# l1 = 'Alex'
# l2 = 'alex'
# l3 = 'GQE'
#
# print(l1>l2, l3>l1, l2>l3,l1==l2,ord('A'))
# for i in range(65,91):
#     print(chr(i),end='\t')

# def first():
#     checks = 0
#     order_index = []
#     orders = []
#
#     menu = ['', 'Americano', 'Americano with milk', 'Latte', 'Cappuccino', 'Espresso']
#     customers = int(input('How many are you?\n'))
#     print(f'{customers} Person')
#
#     for i in range(1, customers + 1):
#
#         print(f'Num 1: Americano - 10$\n'
#               f'Num 2: Americano with milk - 12$\n'
#               f'Num 3: Latte - 15$\n'
#               f'Num 4: Cappuccino -20$\n'
#               f'Num 5: Espresso- 6$\n')
#
#         choice = int(input("Choice: "))
#         if not choice or choice < 1 or choice > 5:
#             print('You don\'t make a choice')
#         else:
#             order_index.append(choice)
#
#         kek = input("Add something else y/n\n")
#
#         while kek.lower() == 'y' or kek.lower() == 'yes':
#             choice = int(input("Choice: "))
#             if not choice or choice < 1 or choice > 5:
#                 print('You don\'t make a choice')
#             else:
#                 order_index.append(choice)
#             kek = input("Add something else y/n\n")
#
#         if i != customers:
#             print('Next person')
#
#     for j in order_index:
#         orders.append(menu[j])
#
#     for i in range(1, len(order_index) + 1):
#         if i == 1:
#             checks += 10
#         elif i == 2:
#             checks += 12
#         elif i == 3:
#             checks += 15
#         elif i == 4:
#             checks += 20
#         elif i == 5:
#             checks += 6
#
#     print('Your order: {} '.format(', '.join(orders)))
#     print(f'Your chang: {checks}$')
#
# def second():
#     start = int(input('Enter start range: '))
#     end = int(input('Enter end range: '))
#     array = []
#     for i in range(start,end+1):
#         for j in range(2,i):
#             if i%j ==0:
#                 break
#         else:array.append(i)
#     print('Simple value in range:')
#     print(array)
#
# def thord():
#
#     st = str(input('Enter your word: '))
#     if st == st[::-1]:
#         print(f'This word {st} - polinom')
#     else: print(f'it\'s not polinom')
#
# def funn():
#     count = []
#     str = 'aabBcde'
#     str = str.lower()
#
#     for i in str:
#         count.append(str.index(i))
#
#     kek = [count[i] for i in range(len(count)) if not i == count.index(count[i])]
#
#     if kek:
#         print(f'{str} -> {len(kek)}')
#         for i in range(len(kek)):
#             print(f'\'{str[kek[i]]}\' - occurs twice')
#     else:
#         print(f'{str} -> 0')
#
# funn()
#/--------------------LESSON6--------------------/

# line1 = 'hello'
# line2 = line1
# print(id(line1),id(line2))
# import random
# import string
#
# line = 'lorem ipsum kek coum ve'
# userLogin = ''.join(random.sample((string.ascii_lowercase),6))
# userPass = ''.join(random.sample((string.ascii_lowercase),6))
# print(f'login:{userLogin}')
# print(f'login:{userPass}')
#
#
# print(string.capwords('lorem ipsum kek coum ve',sep='!'))


# ^[a-Z]$
# ^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-z]+$
# import re

# line = 'Lorem ipsum dolor is sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
# res = re.search(r'[a-z]{1,3}',line)
#
# print(res.start(),res.end())
#


# line = 'Lorem ipsum dolor is sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
# res = (re.findall(r' [a-z]{1,3} ',line)

# print(re.split(r'o',line))
# print(re.sub(r'[a-z]{1-3}','NEW',line))
# pattern = re.compile(r'^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-z]+$')
# print(pattern.findall('bigtigerlesha@gmail.com'))


# pattern= re.compile(r'^(?:0?[1-9]|[12][0-9]|3[01])/(?:0?[1-9]|1[0-2])/(?:19[0-9][0-9]|20[0-9][0-9]) ([0-1][0-9]|2[0-3]):([0-5][0-9]) Description: [a-zA-Z]+$')
# 24/02/2001 23:12 Description: need....
# yout message on 24 feb 2001 at 23:12 oc. can be write
#   your description : need
# num = input('Enter data: ')
# month = [' ','January','February','March','April','May','June','July','August','September','Octobre','November','December']
#
# if pattern.findall(num):
#     data = num.split('/')
#     data = ' '.join(data).split(' ')
#
#
#     print(f'your message on {data[0]} {month[int(data[1])]} {data[2]} at {data[3]}. can be written\nyour {data[4]} {data[5]}')
#/--------------------LESSON7--------------------/

# ls = []
# ls = ['A','B','C']
# # print(*ls)
# # print(ls[0])
#
# for i in ls:
#     print(i,end='\t')
#
# print()
#
# for i in range(0,len(ls)):
#     print(ls[i],end='\t')

# print(f'yes{l1}' if l1 == '1' else 'no')
# print('yes' if True else 'no')

import  random
# l1 = [random.randint(0,10) for i in range(0,10)]
# print(*l1)

# l = list('hello')
# print(l)
# print(*l)
# print(''.join(l))

# l = ['Alex','Den','Nik']
# name1, name2, name3 = l

# l1 = ['Den','Alex']
# l2 = ['Den','Nik']
# if l1 == l2:
#     print('Yes')
# else: print('no')

# l1 = [random.randint(0, 10) for i in range(0, 10)]
# print(l1[::])
#
# l = [
#     ['alex',12],
#     ['den',11],
#     ['jhon',32,['test']]
# ]
#
# for i in l:
#     for j in i:
#         print(j)

# l1 = [random.randint(-5, 10) for i in range(0, 5)]
#
# print(*l1)
#
# minus = 0
# even = 0
# odd = 0
# th = 1
# multbtw = 1
# summ = 0
#
# for i in range(0,len(l1)):
#     if l1[i] < 0:
#         minus += l1[i]
#     if l1[i] % 2 == 0:
#         even += l1[i]
#     else:
#         odd += l1[i]
#     if i % 3 == 0:
#         th *= l1[i]
#
#     e = 0
#     r = 0
#     for i in range(0,len(l1)):
#         if l1[i] > 0:
#             r = i
#             break
#     for i in range(len(l1)-1,0,-1):
#         if l1[i] > 0:
#             e = i
#             break
#
#     summ = sum(l1[r:e])
#
# max_ind = l1.index(max(l1))
# min_id = l1.index(min(l1))
#
# for i in range(min_id,max_ind):
#     multbtw *= l1[i]
#
#
#
# print(f'1:{minus}',
#       f'2:{even}',
#       f'3:{odd}',
#       f'4:{th}',
#       f'5:{multbtw}',
#       f'6:{summ}',sep='\n')

# Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12. Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение может состоять только из трёх частей: число, операция, число. Возможные операции: +, -,*,/

def second():
    l2 = str(input("Enter arithmetic expression: "))

    sign = [i for i in l2 if i == "+" or i == "-" or i == "/" or i == "*"]

    num = l2.split(sign[0])

    print(f"yor arithmetic expression {num[0]}{sign[0]}{num[1]} = {eval(num[0] + sign[0] + num[1])}")


# Користувач заповнює список рандомними елементами
# (числа, букви.. )
# якщо введе пробіл(символ) то введення зупинється та показує на екран:
# сумму чисел, обєднання строк, avg. чисел, має показати два списки,
# які мають числа і строки першого списку, і вивести значення списків
# в вигляді пар тобто : [2,5,9,0,1,9], ["as","sd","gf","fd"]
# as = 2
# sd = 5
# gf = 9
# fd = 0

space =' '
i = 0
digi = []
string = []
array = []
while True:
    list = input("Enter value: ").lower()
    array.append(list)
    i = i + 1
    if list.isdigit():
        digi.append(int(list))
    if list == ' ':
        print('Eexit program')
        break

print(f'sum: {sum(digi)}')
print(f'Array: {space.join(array)}')
print(f'avg: {sum(digi)/len(digi)}')
print(f'Numbers: {space.join(map(str, digi))}')

for i in digi:
    array.remove(str(i))
array.remove(' ')
print(f'Only word: {space.join(array)}')


