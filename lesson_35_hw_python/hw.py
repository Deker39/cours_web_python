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