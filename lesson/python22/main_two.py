# ls1 = (5,2,6,4,1)
# ls2 = 5,2,6,4,1 #tuple
#
# print(type(ls1),type(ls2))
#
# def info() -> tuple:
#     return  5,4,3,2,1
#
# print(info())
#
# from sys import getsizeof
#
# fruits = ['яблоко', 'апельсин', 'банан']

# s1 = {5 ,6 , 7 ,2,10,-2}
# s2 = {11,12,5}
# s1.add(1)
# s1.update({4,5,6})
# # s2 = set([1, 4 ,5 ,6, 7])
# var = s1.pop
#
# print(s1)
#
# s1 = {1,2,3}
# s2 = {3,4,5}
#
# print(s1 | s2, s1.union(s2))
# print(s1 & s2, s1.intersection(s2))
# print(s1 - s2, s1.difference(s2))
# print(s2 - s1, s2.difference(s1))
# print(s1 ^ s2, s1.symmetric_difference(s2))
#
# s3 = {1,2,3,4,5}
# s4 = {2,3,4}
#
# # print(s3.issuperset(s4))
#
#
# x = frozenset([3,4,5])
# print(x)

# def count_nubers(num):
#     count = 0
#     while num > 0:
#         num // 10
#         count += 1
#     return  count

# t = (21,2,34,567,999,1,444)
# ls = ['one number', 'two number', 'three number']
# count_one = 0
# count_two = 0
# count_three = 0
#
# for i in t:
#     if len(str(i)) == 1:
#         count_one +=1
#     elif len(str(i)) == 2:
#         count_two += 1
#     elif len(str(i)) == 3:
#         count_three += 1
#
# print(f'{ls[0]}:{count_one}')
# print(f'{ls[1]}:{count_two}')
# print(f'{ls[2]}:{count_three}')\


import random


def q(p,s):
    global  step_hours
    global count_options
    if p[0] <= 0 or p[0] > size or p[1] <= 0 or p[1] > size or p not in point: # Выход за границы поля и предыдущий шаг
        p = back_point
        count_options.remove(step_hours) #удаление плохого варианта
    else:
        print(f'{s}:{p}:{step_hours}')
        count_options = [1, 2, 3, 4, 5, 6, 7, 8]
        point.remove(p)#удаление шага с  поля
        steps.append(p)
        s -= 1
    return p,s

size = 6 # размер поля
point = []# масив координат - шахмантая доска
for i in range(1,size+1):
    for j in range(1,size+1):
        point.append([i,j])

steps = [] # Пройденій путь
step = len(point)-1 # Количество возможных шагов
point_horse = point[random.randint(0,step)] # Случайное первое место коня
count_options = [1,2,3,4,5,6,7,8] # Индексы возможных шагов
print(point)
print(point_horse)



while step >= 0 and len(count_options):# пока есть свободные шаги и есть выбор

    back_point = point_horse #передыдущий шаг
    step_hours = count_options[random.randint(0,len(count_options)-1)]
    if step_hours == 1:
        point_horse,step = q([point_horse[0] - 2, point_horse[1] + 1],step)
    elif step_hours == 2:
        point_horse,step = q([point_horse[0] - 1, point_horse[1] + 2],step)
    elif step_hours == 3:
        point_horse,step = q([point_horse[0] + 1, point_horse[1] + 2],step)
    elif step_hours == 4:
        point_horse,step = q([point_horse[0] + 2, point_horse[1] + 1],step)
    elif step_hours == 5:
        point_horse,step = q([point_horse[0] - 2, point_horse[1] - 1],step)
    elif step_hours == 6:
        point_horse,step = q([point_horse[0] + 1, point_horse[1] - 2],step)
    elif step_hours == 7:
        point_horse,step = q([point_horse[0] - 1, point_horse[1] + 2],step)
    elif step_hours == 8:
        point_horse,step = q([point_horse[0] - 2, point_horse[1] - 1],step)


print('The end')
print(f'Steps taken: {size*size - step}')
print(f'Passed board cells {steps}')
print(f'Free cells of the board{point}')

