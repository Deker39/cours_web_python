from random import randint
import string
import math
import turtle
import requests
import functools
import time

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
#             print('my number so less...')
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

# def second():
#     l2 = str(input("Enter arithmetic expression: "))

#     sign = [i for i in l2 if i == "+" or i == "-" or i == "/" or i == "*"]

#     num = l2.split(sign[0])

#     print(f"yor arithmetic expression {num[0]}{sign[0]}{num[1]} = {eval(num[0] + sign[0] + num[1])}")


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

# space =' '
# i = 0
# digi = []
# string = []
# array = []
# while True:
#     list = input("Enter value: ").lower()
#     array.append(list)
#     i = i + 1
#     if list.isdigit():
#         digi.append(int(list))
#     if list == ' ':
#         print('Eexit program')
#         break

# print(f'sum: {sum(digi)}')
# print(f'Array: {space.join(array)}')
# print(f'avg: {sum(digi)/len(digi)}')
# print(f'Numbers: {space.join(map(str, digi))}')

# for i in digi:
#     array.remove(str(i))
# array.remove(' ')
# print(f'Only word: {space.join(array)}')



# ls1 = [randint(0,10) for i in range(0,10)]
# ls.remove()
# ls.append()
# ls1 = [5, 7, 6]
# ls2 = ls1.copy()
# ls2[0] = 1
#
# print(ls1)

# num = int(input('Enter number: '))
# #
# # th = ['','M','MM','MMM']
# # h = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
# # t = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
# # o = ['','I','II','III','IV','V','VI','VII','VIII','IX']
# #
# #
# # result = th[(num//1000)] + h[((num%1000)//100)] + t[((num%100)//10)] + o[num%10]
# #
# # print(result)


# order = [5, 5, 9, 8, 5, 9, 2, 9]
#
# max_e = int(input('Enter count: '))
#
# order.reverse()
# for i in order:
#     while order.count(i) > max_e:
#         order.remove(i)
#
# print(order)


# str = 'the-stealth-warrior'
#
# text = 'the-stealth-warrior'
# print(''.join([i.title() if text.index(i) != 0 else i for i in text.split('-')]))
#
# print(str[0]+str.title().replace('-','').replace('_','')[1:] if len(str)>0 else '')

# ls = [0, 7, -5, 1]
# ls1 = ['As','fv','12s']
# ls2 = ['b','cl','12s']
# # print(True if 7 in ls else False)
# # print(ls.index(7))
# ls1.sort(key=str.lower)
# ls2.sort()
# print(ls1,'\n',ls2)

# ls1 = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]
#
# ls2 = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]
#
# ls3 = []
#
#
# i = 0
# while i < len(ls1):
#     j =0
#     temp = []
#     while j < len(ls1[i]):
#         temp.append(ls1[i][j]+ls2[i][i])
#         j +=1
#     ls3.append(temp)
#     i += 1
#
# print(ls3)
# print(*ls)
#
# ls1, ls2, ls3 = ls
#
# print(ls1, ls2, ls3)
#
# print(ls[0][0])
#
# ls1 = [randint(0,10) for i in range(0,10)]
# ls2 = [[randint(0,10) for y in range(0,3)] for j in range(0,5)]
# print(ls2)


#
# full_name= []
# resp = requests.get('https://randomuser.me/api/?results=25')
# json = resp.json()['results']
#
# i = 0
# while i < len(json):
#     r_id = random.randint(10000000,10000000000)
#     # json[i]['id']['value'] = i  # normal numeration 0 to 24
#     # full = str(json[i]['id']['value']).center(20) + " " + json[i]['name']['title'].center(13) +  " " + json[i]['name']['first'].center(15) + " " + json[i]['name']['last'].center(14)
#     full = str(json[i]['id']['value'] if json[i]['id']['value'] is not None and json[i]['id']['value'].isdigit() else r_id).center(20)  + " " + json[i]['name']['title'].center(13) + \
#            " " + json[i]['name']['first'].center(15)  + " " + json[i]['name']['last'].center(14)
#
#
#     if json[i]['id']['value'] is None:
#         json[i]['id']['value'] = r_id
#
#     full_name.append(full)
#     i += 1
#
# print('ID:'.center(20) + 'Title:'.center(15) +  'First:'.center(15) + 'Last:'.center(15))
# for i in full_name:
#     print(i)
#
# print()
# user_to_find = input('enter id: ')
# for j in full_name:
#     if j.find(user_to_find) > 0:
#         print(f'find user : {j}')
#         print(f'street: {json[i.find(user_to_find)]["location"]["street"]["name"]} №{json[i.find(user_to_find)]["location"]["street"]["number"]}\n'
#               f'city: {json[i.find(user_to_find)]["location"]["city"]}\n'
#               f'state: {json[i.find(user_to_find)]["location"]["state"]}\n'
#               f'country: {json[i.find(user_to_find)]["location"]["country"]}\n'
#               f'email: {json[i.find(user_to_find)]["email"]}\n'
#               f'login: {json[i.find(user_to_find)]["login"]["username"]}\n'
#               f'password: {json[i.find(user_to_find)]["login"]["password"]}')


# print(json['results'])
# print(resp.status_code)
# print(resp.headers['Content-Type'])
# print(resp.text)

# def sum_my_number()

# def foo1():
#     print('foo1')
# breakpoint()
# foo1()

# A = int(input('A: '))
# B = int(input('B: '))
# C = int(input('C: '))
#
# if A==0: A = 1
# if B==0: B = 1
# if C==0: C = 1
#
# D = B*B - 4 * A * C
#
#
# x = 0
# print(D)
# if D > 0:
#     x1 = ((-B) + math.sqrt(D)) / 2 * A
#     x2 = ((-B) - math.sqrt(D)) / 2 * A
#     print(f'x1: {x1}')
#     print(f'x2: {x2}')

# def foo(name):
#     print(f'foo started - {name}')
#
# foo('Alpha')

# def foo(*args):
#     c = 0
#     sum = 0
#     for i in args:
#         c +=1
#         sum += i
#     return  sum/c
#
#
# print(foo(5,5,5,5))


# num = 5
#
# def  wellcome_admin(name):
#     print(f"Admin: {name}")
#
# def  wellcome_user(name):
#     print(f"Hi user: {name}")
#
#
# def wellcome_hr(name):
#     print(f"Hi pr: {name}")
#
# def foo(name,func):
#     func(name)
# #
# def foo():
#     n = 5
#     def foo2():
#         nonlocal  n
#         global  num
#
#         num = -5
#         n += 1
#         l = 5
#         print(l)
#         print(num)
#         print(__name__)
#
#     return  foo2()
#
# def main():
#
#    foo('Alex',wellcome_user)
#
# if __name__ == '__main__':
#     main()
#
# def par(num):
#     str_num = str(num)
#     l1 = str_num[int((len(str_num))/2):]
#     l2 = list(str_num[0:int((len(str_num))/2)])
#     l2.reverse()
#     l2 = ''.join(l2)
#     print(l1)
#     print(l2)


# def main():
#     par(12344321)

# def pww(n,s):
#     return  n if s==1 else n * pww(n,s-1)
#
#
# def main():
#     print(pww(2,3))
#     print(qq(2,3))


# def sun(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# def div(a,b):
#     return a/b
#
# def mult(a,b):
#     return a*b
#
# def mess(func):
#     print(f"Result: {func(5,6)}")


# def calc(a, b, op):
#     print(f'Result {op(a,b)}')
#
# def main():
    # [mess(i) for i  in [sun, sub, div, mult]]

    # mess = lambda: print('hello')
    # mess()
    #
    # pww = lambda x: x*x
    # print(pww(5))
    #
    # calc(2, 2, lambda a, b: a + b)
    # calc(2, 2, lambda a, b: a / b)
    #
    #
    # f = lambda  x: x * x
    #
    # ls = [5,6,7,3,2]
    # ls.sort(key= lambda x:x > 5)
    # print(*ls)
    #
    # # for i in ls:
    #     print((lambda  x: x * x)(i))

    # def sum(n):
        # return  n+n

    # ls1 = [1, 2, 3, 4, 5]
    # ls2 = [5, 4, 3, 2, 1]
    # ls3 = ['user1234','user2','user34','34']
    # ls3 = ['ale-op','lio-a','cell-1']
    # res = list(map(lambda x: x,ls1))


    # print(list(map(list, ls3)))
    # print(list(map(lambda x: x.replace('-',''),ls3)))

    # print(list(filter(lambda x: x.find('o') > 0 ,ls3)))

    # l = (54,0,-12,100, -9)

    # ls2 = [
    #     ['Alex',20],
    #     ['Jhon', 30],
    #     ['Den', 6],
    #     ['Ron', 10],
    # ]
    #
    # res = sorted(ls2,key= lambda x: x[1])
    # print(*res)

    # userLogs = ['123user45', 'USERstudent', '56use3', 'user-23', 'adminUs']
    # userPass = ['111', 'abc', '2345', '45fg', 'dffdg']
    #
    # print(list(zip(userLogs,userPass)))

    # for log, passw in zip(userLogs, userPass):
    #     print("login: {} — password: {}".
    #           format(log, passw))

    #
    # def sum(a, b):
    #     return a + b
    #
    # print(sum(5, 5))
    #
    # # partial(func..., args,**kwargs)
    #
    # s1 = functools.partial(sum, b = 5)
    # s2 = functools.partial(sum, 5)
    #
    # print(s1(2),s2(5))
    # print(s1.keywords)

# if __name__ == '__main__':

    # main()

#################### nonlocal, curring, wrapper

# def outer(text):
#     v = "hello " + text
#
#     def inner(param):
#         print(v + param)
#
#     return inner
#
# t = outer("data")
#
# t(" t")

# def outer():
#     i =0
#
#     def inner( ):
#         nonlocal  i
#         i += 1
#         return  i
#     return inner
#
# c = outer()
# for i in range(10):
#     print(c())

# def outer(power):
#     i = power
#
#     def inner(ls):
#         nonlocal  i
#         temp = []
#         for item in ls:
#             x = item
#             for p in range(1, i):
#                 item *= x
#             temp.append(item)
#         return temp
#     return inner
#
# c = outer(5)
# print(c([1,2,3,4,5]))
# print(c([2,2,2]))

# def foo(x1,x2,x3) -> foo(x1)(x2)(x3)

# def outer(user):
#
#     def inner(ms):
#         print(f'Hello {user} -- {ms}')
#
#     return inner
#
# sendMess = outer('Admin')
#
# sendMess('text')
#
# outer('User')('asd')
# outer('User')('text')

# def foo1(ms1):
#     def foo2(ms2):
#         def foo3(ms3):
#             def foo4(ms4):
#                 print(f'{ms1} \t{ms2} \t{ms3} \t{ms4}')
#             return foo4
#         return  foo3
#     return foo2
# fo = foo1('ms1')
# fo('ms2')('ms3')('ms4')
#
# fo = foo1('ms1')('ms2')
# fo('ms3')('ms4')
#
# fo = foo1('ms1')('ms2')('ms3')
# fo('ms4')
#
# fo = foo1('ms1')('ms2')('ms3')('ms4')


# def outer(n):

#     def inner(n1=2):
#         return n * n1
#
#     return  inner()
#
# print(outer(5))

# def wel(func): #func default
#
#     def inner(ls):
#         for user in ls:
#             print(func(user) + user)
#
#     return inner
#
# @wel
# def show(user):
#     if user.find('admin') >= 0:
#         return 'Welcome! '
#     elif user.find('user') >=0:
#         return 'Hello! '
#     else:
#         return 'Need reg? '


# show(['admin Alex','user Jhon','Den','admin Nick'])


# def get_diff(func):
#     def start():
#         s = time.time()
#         func()
#         diff = time.time() - s
#         return diff
#     return start
#
# @get_diff
# def get_data():
#     requests.get('https://randomuser.me/api/?results=25').json()
#
# print(get_data())

# def get_diff(func):
#
#     def statr():
#
#         while True:
#             n = int(input('s: '))
#             s = time.time()
#             func(n)
#             diff = time.time() - s
#             print(diff)
#     return statr

# @get_diff
@functools.lru_cache
def get_data(n):
    s = time.time()

    diff = time.time() - s
    print(f'fact {math.factorial(n)}')
    print(diff)

while True:
    n = int(input('s: '))
    get_data(n)
