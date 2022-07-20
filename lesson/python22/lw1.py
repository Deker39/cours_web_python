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