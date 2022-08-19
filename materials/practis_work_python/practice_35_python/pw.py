# Exercise_1
def first():
    side = int(input('Enter side of a square: '))
    for x in range(0, side):
        print(side * '*')
# Exercise_2
def second():
    weight = int(input('Enter weight side of a square: '))
    height = int(input('Enter height side of a square: '))
    for x in range(0, height):
        print(weight * '*')
# Exercise_3
def third():
    side = int(input('Enter side of a square: '))
    for x in range(0, side):
        print (side * '*' if x == 0 or x == side - 1 else '*' + (side - 2) * ' ' + '*')
# Exercise_4
def fourth():
    weight = int(input('Enter weight side of a square: '))
    height = int(input('Enter height side of a square: '))
    for x in range(0, height):
        print(weight * '*' if x == 0 or x == height - 1 else '*' + (weight - 2) * ' ' + '*')