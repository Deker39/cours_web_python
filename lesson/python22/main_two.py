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

#import random
#
#
# def q(p,s):
#     global  step_hours
#     global count_options
#     if p[0] <= 0 or p[0] > size or p[1] <= 0 or p[1] > size or p not in point: # Выход за границы поля и предыдущий шаг
#         p = back_point
#         count_options.remove(step_hours) #удаление плохого варианта
#     else:
#         print(f'{s}:{p}:{step_hours}')
#         count_options = [1, 2, 3, 4, 5, 6, 7, 8]
#         point.remove(p)#удаление шага с  поля
#         steps.append(p)
#         s -= 1
#     return p,s
#
# size = 6 # размер поля
# point = []# масив координат - шахмантая доска
# for i in range(1,size+1):
#     for j in range(1,size+1):
#         point.append([i,j])
#
# steps = [] # Пройденій путь
# step = len(point)-1 # Количество возможных шагов
# point_horse = point[random.randint(0,step)] # Случайное первое место коня
# count_options = [1,2,3,4,5,6,7,8] # Индексы возможных шагов
# print(point)
# print(point_horse)
#
# while step >= 0 and len(count_options):# пока есть свободные шаги и есть выбор
#
#     back_point = point_horse #передыдущий шаг
#     step_hours = count_options[random.randint(0,len(count_options)-1)]
#     if step_hours == 1:
#         point_horse,step = q([point_horse[0] - 2, point_horse[1] + 1],step)
#     elif step_hours == 2:
#         point_horse,step = q([point_horse[0] - 1, point_horse[1] + 2],step)
#     elif step_hours == 3:
#         point_horse,step = q([point_horse[0] + 1, point_horse[1] + 2],step)
#     elif step_hours == 4:
#         point_horse,step = q([point_horse[0] + 2, point_horse[1] + 1],step)
#     elif step_hours == 5:
#         point_horse,step = q([point_horse[0] - 2, point_horse[1] - 1],step)
#     elif step_hours == 6:
#         point_horse,step = q([point_horse[0] + 1, point_horse[1] - 2],step)
#     elif step_hours == 7:
#         point_horse,step = q([point_horse[0] - 1, point_horse[1] + 2],step)
#     elif step_hours == 8:
#         point_horse,step = q([point_horse[0] - 2, point_horse[1] - 1],step)
#
# print('The end')
# print(f'Steps taken: {size*size - step}')
# print(f'Passed board cells {steps}')
# print(f'Free cells of the board{point}')

# list, tuple
# name -> 'alex

# v1 = {'name':'alex'}
# print(v1['name'])

# person = {'name':'Alex','age':20}

# print(person.get('asfsf','Unkown key'))
# print(person.popitem())
# print(person)

# for i in person:
#     print(f'Key: {i}, value: {person[i]}')
#
# for key,value in person.items():
#     print(f'Key: {key}, value: {value}')
#
# for v in person.values():
#     print(f'Key: ?, value: {v}')
#
# for k in person.keys():
#     print(f'Key: {k}, value: ?')

# persons = {
#     'Alex':{
#         'second_name':'value1',
#         'age':'value2'
#     },
#     'John':{
#             'second_name':'value3',
#             'age':'value4'
#         }
# }
#
# for k,v in persons.items():
#     print(f'\nKey: {k} Value ', end=" ")
#     for  k1,v1 in v.items():
#          print(f'\n\t Key:{k1} Value: {v1}' ,end=' ')

### 1 ###
# capitals = {'Ukraine':'Kyiv'}
#
# def menu_first():
#     print('Choose action:\n'
#           '1.Add capital by country\n'
#           '2.Remove capital by country\n'
#           '3.Search capital by country\n'
#           '4.Replace capital by country\n'
#           '5.Show all capital bu counrty'
#           '6.Exit')
#     return input('Enter choose: ')
#
# def add_item():
#     global capitals
#     country = input('Enter name country: ')
#     capital = input('Enter name capital: ')
#     capitals[country] = capital
#
# def main_first():
#     choose = ''
#     while not choose.startswith('6'):
#         choose = menu_first()
#         if choose.startswith('1'):
#             add_item()
#         elif choose.startswith('2'):
#             country = input('Enter name country to delete: ')
#             if country in capitals:
#                 del capitals[country]
#             else:
#                 print('Unknown country')
#         elif choose.startswith('3'):
#             country = input('Enter name country to search: ')
#             if country in capitals:
#                 print(f'Fiend: \n\t Country: {country} \t Capitl: {capitals[country]}')
#             else: print('Unknown country')
#         elif choose.startswith('4'):
#             country = input('Enter new name country to replace: ')
#             if country in capitals:
#                 add_item()
#             else:
#                 print('Unknown country')
#         elif choose.startswith('5'):
#             if len(capitals) > 0:
#                 for k, v in capitals.items():
#                     print(f'Country: {k}\t Capital: {v}')
#         elif choose.startswith('6'):
#             print("Good buy")
#         else: print('Error')

# ### 2 ###
# dictionary = {'hello':'bonjur'}
#
# def add_word():
#     global dictionary
#     english_word = input('Enter a word of english: ')
#     french_woed = input('Enter a word of french: ')
#     dictionary[english_word] = french_woed
#
# def menu_second():
#     print('Choose action:\n'
#           '1.Add a word of english and french\n'
#           '2.Remove a word of english and french\n'
#           '3.Search a word\n'
#           '4.Replace a word\n'
#           '5.Show dictionary\n'
#           '6.Exit')
#     return input('Enter choose: ')
#
# def main_second():
#     choose = ''
#     while not choose.startswith('6'):
#         choose = menu_second()
#         if choose.startswith('1'):
#             add_word()
#         elif choose.startswith('2'):
#             english_word = input('Enter a word of english: ')
#             if english_word in dictionary:
#                 del dictionary[english_word]
#             else:
#                 print('Unknown english word')
#         elif choose.startswith('3'):
#             english_word = input('Enter a word of english to search: ')
#             if english_word in dictionary:
#                 print(f'Fiend: \n\t English Word: {english_word} \t French Word: {dictionary[english_word]}')
#             else:
#                 print('Unknown english word')
#         elif choose.startswith('4'):
#             english_word = input('Enter a word of english to replace: ')
#             if english_word in dictionary:
#                 add_word()
#             else:
#                 print('Unknown english word')
#         elif choose.startswith('5'):
#             if len(dictionary) > 0:
#                 for k, v in dictionary.items():
#                     print(f'Country: {k}\t Capital: {v}')
#         elif choose.startswith('6'):
#             print("Good buy")
#         else: print('Error')
#
#
# firma = {
#     1:{
#         'First Name':'Alex',
#         'Last Name': 'Holenko',
#         'Tel':'+380986071514',
#         'Email':'kek@gmail.com',
#         'Post':'Programmer',
#         'Number cabinet': '356',
#         'Skype':'dek33'
#     }
#
# }
#
# def add_person():
#
#     firs_name = input('Enter a firs name: ')
#     last_name = input('Enter a last name: ')
#     tel = input('Enter a tel number: ')
#     email = input('Enter a email: ')
#     post = input('Enter a post: ')
#     number_cabinet = input('Enter a number cabinet: ')
#     skype = input('Enter a skype: ')
#     return {'Firs Name':firs_name,'Last Name':last_name,'Tel':tel,'Email':email,'Post':post,'Number cabinet':number_cabinet,'Skype':skype}
#
# def menu_third():
#     print('Choose action:\n'
#           '1.Add a information of man\n'
#           '2.Remove a information of man\n'
#           '3.Search a information of man\n'
#           '4.Replace a information of man\n'
#           '5.Show information of people\n'
#           '6.Exit')
#     return input('Enter choose: ')
#
# def main_third():
#     choose = ''
#     while not choose.startswith('6'):
#         choose = menu_third()
#         if choose.startswith('1'):
#             firma[len(firma)+1] =add_person()
#         elif choose.startswith('2'):
#             last_name = input('Enter a last name: ')
#             for k,v in firma.items():
#                 if last_name in v['Last Name']:
#                     del firma[k]
#                     break
#                 else:
#                     print('Unknown Last name')
#         elif choose.startswith('3'):
#             last_name = input('Enter a last name: ')
#             for k, v in firma.items():
#                 if last_name in v['Last Name']:
#                     print(f'\nPerson: {k} Info ', end=" ")
#                     for k1, v1 in v.items():
#                         print(f'\n\t {k1} : {v1}', end=' ')
#                     print()
#                 else:
#                     print('Unknown Last name')
#         elif choose.startswith('4'):
#             last_name = input('Enter a last name: ')
#             for k, v in firma.items():
#                 if last_name in v['Last Name']:
#                     firma[k] = add_person()
#                 else:
#                     print('Unknown Last name')
#         elif choose.startswith('5'):
#             for k,v in firma.items():
#                 print(f'\nPerson: {k} Info ', end=" ")
#                 for  k1,v1 in v.items():
#                      print(f'\n\t {k1} : {v1}' ,end=' ')
#             print()
#         elif choose.startswith('6'):
#             print("Good buy")
#         else:
#             print('Error')
# if __name__ == '__main__':
#     # main_second()
#     main_third()
#
# def find_max(ls):
#     max_item = ls[0]
#     i = 0
#
#     def find(item):
#         nonlocal max_item, i, ls
#
#         if max_item < ls[i]:
#             max_item = ls[i]
#         elif i < len(ls):
#             i +=1
#             find(i)
#         return  max_item
#
#     find(max_item)

    # return max_item
#
# ls = [5,4,3,12,2,6,356]
# print(find_max(ls))


# line = '01224gevefre@214'
#
# print(int(''.join((list(map(lambda x: x if x.isdigit() else '', line))))))
# alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
# l = 'ABC'
#
# def rot13(line,):
#     res = ''
#     for i in line:
#         res += chr(ord(i)+13)
#     return res
#
#
# print(rot13(l))

#def likes(names):
#     if len(names) == 0:
#         return 'no one likes this'
#     else:
#         if len(names) == 1:
#             return f'{names[0]} likes this'
#         elif  len(names) == 2:
#             return f'{names[0]} and {names[1]} like this'
#         elif len(names) == 3:
#             return f'{names[0]}, {names[1]} and {names[2]} like this'
#         elif len(names) == 4:
#             return f'{names[0]}, {names[1]} and {len(names)-2} others like this'

# print(likes(['Galatea', 'Quincy Rosenkreutz', 'Nigel', 'Linna Yamazaki', 'Sylia Stingray', 'Leon McNichol']))
# import re
#
# def is_valid_IP(string):
#     return  True if re.search(r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",string) != None else False
#
#
# print(is_valid_IP('12.255.56.1'))
# print(is_valid_IP(''))
# print(is_valid_IP('abc.def.ghi.jkl'))
# print(is_valid_IP('123.456.789.0'))
# print(is_valid_IP('12.34.56'))
# print(is_valid_IP('123.045.067.089'))

# open(file)
# file - path,abs/rel
# mode - 'r' -read, 'w' - write, 'a' - append, 'b' - binary
# encoding - 'utf-8

# try:
#     f = open('myfile.txt', 'r')
#     try:
#
#         l = f.readline()
#         while l:
#             print(l,end='')
#             l = f.readline()
#
    # except Exception as ex:
    #     print(f'error2: {str(ex)}')
    # finally:
    #     f.close()
# except Exception as e:
#     print(f'error1 {str(e)}')
# import time
#
#
# print('Loading', end=' ')
# for i in range(0,4):
#     time.sleep(1)
#     print(' . ', end='')
#
# print('\nAlina mivina')

# count = 0
# f = open('myfile.txt','r')
# is_insert = False
# ls = []
# for i in f:
#     ls.append(i)
#     if i.count(',') <= 0 and not is_insert:
#         is_insert = True
#         ls.append('*************\n')
# if not is_insert:
#     ls.append('*************\n')
#
# print(*ls)
# f.close()

# while True:
#     try:
#         # n = int(input('Enter number: '))
#         f =open('c\:adad')
#         break
#     except OSError as e:
#         print(e.args)
#         print(f'Only number...')
#
# print('the end')
# ls_my_f = []
# words = []
# new_ls = []
#
#
# with open('myfile.txt','r') as f:
#     ls_my_f = f.read()
#
# with open('words.txt','r') as f:
#     words = map(lambda x: x.replace('\n',''),f.readlines())
#
# if ls_my_f and words:
#     for word in words:
#         ls_my_f = ls_my_f.replace(word,' ')
#
#     with open('myfile.txt', 'w') as f:
#         f.write(ls_my_f)

import os

# os.mkdir(forlder_path_and_name)  - creat folder
# os.mkdir('hello')
# os.rmdir(folder_path) - remove folder
# os.rmdir('forlder_path_and_name')
# os.rename(folder/forlder_path_rename_old/file_path_rename_new) -change name
# os.rename('hello', 'new/forlder_path_and_name')
# os.rmdir('new/forlder_path_and_name')
# print(os.name)
# print(os.environ)
# print(os.getlogin())
# print(os.getpid())
# print(os.uname())
# print(os.chdir())
# print(os.getcwd()) - return current path
# os.chdir('new')# change work dir
# print(os.getcwd())
# print(os.path)


import shutil

# move dir , up dir , removem create , create file, rename file
def show_content():
    ls =  os.listdir((os.getcwd()))
    for ind,item in enumerate(ls):
        print(f'{"file" if  os.path.isfile(item) else "folder"}\t #{ind+1}: {item} ')

def menu():
    print('Current path: ', os.getcwd(), end='\n')
    show_content()
    print('Specific content: ')
    os.listdir(os.getcwd())
    print('''
1. Move to dir.
2. Up dir.
3. Remove folder/file.
4. Create dir/file.
5. Rename folde/file.
6. Exit
               ''')
    try:
        return int(input('Enter action: '))
    except Exception as exc:
        print(f'You can enter only number! Error - {exc}')


def move_dir():
    path = input('Enter path to move(abs/rel): ')
    if os.path.exists(path):
        os.chdir(path)
    else:
        print("Error path")

def up_dir():
    os.chdir(os.path.dirname(os.getcwd()))

def remove_dir():
    path = input('Enter path to remove(abs/rel): ')
    if os.path.isfile(path):
        os.remove(path)
        print(f'File deleted: {path}')
        return
    if os.path.isdir(path):
        if input('You sure delete this folder? Because folder is not empty\nEnter y\\n ').lower()  == 'y':
             shutil.rmtree(path)
             print(f'Folder delete: {path}')
    else:
        print('Unknown path!')

def creat_item():
    choose  = int(input('Enter what you want creat:\n1. Folder\n2. File\nEnter choose: '))
    if choose == 1:
        name = input('Enter name of folder: ')
        if not os.path.exists(name):
            os.mkdir(name)
        else:
            print('Folder exists!')
    elif choose == 2:
        name = input('Enter name of file: ')
        if not os.path.exists(name):
            open(name,'w')
        else:
            print('File exists!')

def rename_item():
    choose  = int(input('Enter what you want rename:\n1. Folder\n2. File\nEnter choose: '))
    if choose == 1:
        old_name = input('Enter old name of folder: ')
        new_name = input('Enter new name of folder: ')
        os.renames(old_name,new_name  if os.path.exists(old_name) else 'Folder not exists!')
    elif choose == 2:
        old_name = input('Enter old name of file: ')
        new_name = input('Enter new name of file: ')
        os.renames(old_name, new_name if os.path.exists(old_name) else 'File not exists!')


def main():
    while True:
        choose = menu()
        if choose == 1:
            move_dir()
        elif choose == 2:
            up_dir()
        elif choose == 3:
            remove_dir()
        elif choose == 4:
            creat_item()
        elif choose == 5:
            rename_item()

PATH =  os.getcwd()

if __name__ == '__main__':
    main()
