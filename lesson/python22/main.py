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

num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def number(bal):
    if 1 <= bal < 19:
        return num2words1[bal]
    elif 20 <= bal <= 99:
        tens = bal//10
        below_ten = bal%10
        if below_ten == 0:
            return num2words2[tens-2]
        else: return num2words2[tens-2] + '-' + num2words1[below_ten]
    else:
        print("Number out of range")



balans = input("Enter your balans: ")  # баланс от 0 до 100
print(f'Your balanse:{balans}$, please make a choice')
print(f'Num 1: Americano - 10$\n'
      f'Num 2: Americano with milk - 12$\n'
      f'Num 3: Latte - 15$\n'
      f'Num 4: Cappuccino -20$\n'
      f'Num 5: Espresso- 6%\n')

choice = int(input("Choice: "))

if not choice or len(balans) > 3 or 1 <= choice >6: print('You don\'t make a choice')
else:
    if int(balans) > choice:
         if choice == 1: print(f'your order: Americano\nyour change: {int(balans) -10}-{number(int(balans) -10)}')
         elif choice == 2: print(f'your order:Americano with milk\nyour change: {int(balans) -12}-{number(int(balans) -12)}')
         elif choice == 3: print(f'your order: Latte\nyour change: {int(balans) -15}-{number(int(balans) -15)}')
         elif choice == 4: print(f'your order: Cappuccino\nyour change: {int(balans) -20}-{number(int(balans) -20)}')
         elif choice == 5: print(f'your order: Espresso\nyour chang: {int(balans) - 6}-{number(int(balans) - 6)}')
    else: print('you poor')

