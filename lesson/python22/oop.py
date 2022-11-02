#class Name:
    # ferld = ...
import hashlib
# class Person:
#
#     def __init__(self,name,age):
#         # public
#         self.name = name
#         # private
#         self.__age = age
#         # protected = private
#         # self._p = 5
#
#     def info(self):
#         print(f'Name:{self.name} - - Age:{self.__age}')
#
#
# p1 = Person('Alex',23)
# p1.info()
#
# p1.info()

# class Human:
#     h = 6
#
#     def __init__(self,full_name,bd,phone,city,country,address):
#         self.__full_name = full_name
#         self.__bd = bd
#         self.__phone = phone
#         self.__city = city
#         self.__country = country
#         self.__address = address
#
#     def info(self):
#
#         return f'{self.__full_name},{self.__bd},{self.__phone},{self.__city},{self.__country},{self.__address}'
#
#     def __format__inf(self):
#         print('Info block')
#
#     def __str__(self):
#         return f'{self.__full_name},{self.__bd},{self.__phone},{self.__city},{self.__country},{self.__address}'
#
#     def get__full_name(self):
#         return  "Name " + self.__full_name
#
#     def set__full_name(self,fname):
#         if isinstance(fname,str) and 3 < len(fname) < 30:
#             self.__full_name = fname
#         else:
#              raise  ValueError(f'{fname} id wrong data...')
#
#
#
# h1 = Human('jhone','22.22.22','+124124124','Lviv','Ukraine','adders')
# print(h1)
# h1.set__full_name('Alex')
# print(h1)


# class Number:
#     def  __init__(self,number):
#         self.number = number
#     @staticmethod
#     def to_pow(n1,n2):
#         print(n1**n2)
#
#
#
# n1 = Number(5)
#
# n1.to_pow(3,2)

# class Person:
#
#     id = 0
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age

    # @classmethod
    # def method_1(cls):
    #     print(cls.id)
    #     cls.id = 4
    #     print(cls.id)

    # @staticmethod
    # def method_2(name):
    #     print(f'Hello, {name}')

    # def method_3(self):
    #     print(f' hello, {self.name}')



# p1 = Person('Den',20)
# print(p1.id)
# p1.id = 5
# print(p1.id)
# print(Person.id)
# p1.method_1()
# p1.id  = 5
# print(p1.id)
# p1.method_2('Alex')

# class Human:
#     def __init__(self,name):
#         self._name = name
#     def show(self):
#         print(f'{self._name}')
#
# class Employee(Human):
#     def __init__(self,name,salary):
#         super().__init__(name)
#         self.salary = salary
#
#     def show(self):
#         print(f'{self._name}, {self.salary}')
#
#
# h1 = Human('name1')
#
# e1 = Employee('name2',124)
# e1.show()


# class Human:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(f'{self.name}')
#
# class Worker:
#     def __init__(self,salary):
#         self.salary = salary
#     def show(self):
#         print(f'{self.salary}')
#
#
# class Employee(Human,Worker):
#     def __init__(self,name,salary):
#         Human.__init__(self,name)
#         Worker.__init__(self,salary)
#
#
#     # def show(self):
#     #     print(f'{self.name}, {self.salary}')
#
#
#
# p1 = Employee('den',200)
#
# Worker.show(p1)
# Human.show(p1)

# class A:
#     def __init__(self,a):
#         self.a = a
#     def hi(self):
#         print('A')
# class B(A):
#     def __init__(self, b,a):
#         A.__init__(self,a)
#         self.b = b
#
#     def hi(self):
#         print('B')
# class C(A):
#     def __init__(self,c,a):
#         A.__init__(self,a)
#         self.c =c
#
#     def hi(self):
#         print('C')
#
# class D(B,C):
#     def __init__(self,d,b,c,a):
#         B.__init__(self,b,a)
#         C.__init__(self,c,a)
#         self.d = d
#     def hi1(self):
#         C.hi(self)
#     def info(self):
#         print(f'{self.d},{self.a},{self.b},{self.c}')
#
#
# d = D(1,2,3,4)
# d.info()
# # d.hi()
# # d.hi1()
# print(D.mro())


# class Number:
#     def __init__(self,n):
#         self.n = n
#         self.counter = 0
#         # print(f'object: {self} created')
#
    # def __new__(cls, *args, **kwargs):
    #     print(f'new obj for: {cls} ')
    #     return super().__new__(cls)
    #
    # def __call__(self, *args, **kwargs):
    #     print('its magik from call')
    #     self.counter += 1
    #
    # def __str__(self):
    #     return  f'n = {self.n}. counter = {self.counter}'
    #
    # def __repr__(self):
    #     return f'AAAAA'
    #
    # def __len__(self):
    #     return self.counter
    #
    # def __abs__(self):
    #     return  abs(self.n)
    #
#     def __add__(self, other):
#         if isinstance(other,int):
#             return Number(self.n + other)
#         elif isinstance(other, Number):
#             return Number(self.n + other.n)
#         else:
#             raise Exception('Unkomon type')
#
#     def __sub__(self, other):
#         if isinstance(other,int):
#             return Number(self.n - other)
#         elif isinstance(other, Number):
#             return Number(self.n - other.n)
#         else:
#             raise Exception('Unkomon type')
#
#     def __mul__(self, other):
#         if isinstance(other,int):
#             return Number(self.n * other)
#         elif isinstance(other, Number):
#             return Number(self.n * other.n)
#         else:
#             raise Exception('Unkomon type')
#
#     def __truediv__(self, other):
#         if isinstance(other,int):
#             return Number(self.n / other)
#         elif isinstance(other, Number):
#             return Number(self.n / other.n)
#         else:
#             raise Exception('Unkomon type')
#
#     def __floordiv__(self, other):
#         if isinstance(other, int):
#             return Number(self.n // other)
#         elif isinstance(other, Number):
#             return Number(self.n // other.n)
#         else:
#             raise Exception('Unkomon type')
#
#     def __mod__(self, other):
#         if isinstance(other, int):
#             return Number(self.n % other)
#         elif isinstance(other, Number):
#             return Number(self.n % other.n)
#         else:
#             raise Exception('Unkomon type')
#
#     def __radd__(self, other):
#         if isinstance(other,int):
#             return Number(self.n + other)
#         elif isinstance(other, Number):
#             return Number(self.n + other.n)
#         else:
#             raise Exception('Unkomon type')
#
#     def __iadd__(self, other):
#         if isinstance(other,int):
#             self.n += other
#             return  self
#
#     def __eq__(self, other):
#         return  self.n == other
#
#     def __ne__(self, other):
#         return not self.n == other
#
#     def __lt__(self, other):
#         return  self.n < other
#     def __gt__(self, other):
#         return  self.n > other
#     def __le__(self, other):
#         return  self.n <= other
#     def __ge__(self, other):
#         return  self.n >= other
#     # def __del__(self):
#     #     print(f'object: {self} deleted')
#
# n1 = Number(5)
# n2 = Number(10)
# # n1()
# # n1()
# # print(len(n1))
# # print(abs(n2))
#
# print((n1+n2).n)
# print((n1-n2).n)
# print((n1*n2).n)
# print((n1/n2).n)
# print((n1//n2).n)
# print((n1%n2).n)
# print(n2 == 10)
# # print(n1.counter, n2.counter)

#TODO Functor

# class StripString:
#     def __init__(self,chars):
#         self.__chars = chars
#
#     def __call__(self, st):
#         return st.strip(self.__chars)
#
# s1 = StripString('!@#$%^')
# print(s1('Hello !@#$%^'))

# class Circle():
#
#     def __init__(self,r):
#         self.r = r
#
#     def __add__(self, other):
#         return self.r + other
#
#     def __iadd__(self, other):
#         self.r += other
#         return  self.r
#
#     def __sub__(self, other):
#         self.r -= other
#         return self.r
#
#     def __isub__(self, other):
#         return self.r - other
#
#     def __eq__(self, other):
#         return self.r == other
#     def __lt__(self, other):
#         return  self.r < other
#     def __gt__(self, other):
#         return  self.r > other
#     def __le__(self, other):
#         return  self.r <= other
#     def __ge__(self, other):
#         return  self.r >= other
#
# o1 = Circle(5)
# o2 = Circle(3)
# print(o1+3)
# print(o1-3)
# o1 +=1
# o2 -=2
# print(o1)
# print(o2)
# print(o1==o2)
# print(o1<o2)
# print(o1>o2)
# print(o1<=o2)
# print(o1>=o2)
#
# class Complex(object):
#
#     def __init__(self, arg, static):
#         self.arg = arg
#         self.static = static
#         # Formats our results
#         print(self.arg + self.static)
#
#     def __add__(self, other):
#         return Complex(self.arg + other.arg, self.static + other.static)
#
#     def __sub__(self, other):
#         return Complex(self.arg - other.arg, self.static - other.static)
#
#     def __mul__(self, other):
#         return Complex((self.arg * other.arg) - (self.static * other.static),(self.static * other.arg) + (self.arg * other.static))
#
#     def __truediv__(self, other):
#         r = (other.arg ** 2 + other.static ** 2)
#         return Complex((self.arg * other.arg - self.static * other.static) / r,(self.static * other.arg + self.arg * other.static) / r)
#
# a1 = Complex(1, 5j)
# a2 = Complex(6, 2j)
#
# # Add
# a1 + a2
# # Subtract
# a1 - a2
# # Multiply
# a1 * a2
# # Divide
# a1 / a2
# Decorator

# def foramt(foo):
#     def inner(*args):
#         print('*******')
#         foo(*args)
#         print('*******')
#     return  inner
#
#
# @foramt
# def foo(name,age):
#     print(f'Hello for foo {name} age {age}')
#
# # def format_foo(foo):
# #     print('*******')
# #     foo()
# #     print('*******')
#
# foo('Den',25)

# def format(func):
#     def inner(a,b):
#         print('******')
#         res = func(a,b)
#         print('******')
#         return f'Result: {res}'
#     return  inner
#
# @format
# def foo(a,b):
#     return  a+b
#
# print(foo(5,25))


# class  CountClass:
#     def __init__(self,func):
#         self.func= func
#         self.counter = 0
#     def __call__(self, *args, **kwargs):
#         self.counter += 1
#         print(f'Call {self.func.__name__}:{self.counter}')
#         return self.func(*args)
#
#
# @CountClass
# def foo(name):
#     print(f'Hello - {name}')
#
#
# foo('Den')
# foo('Den')
# foo('Den')

# class Repeter:
#     def __init__(self,num):
#         self.num= num
#
#     def __call__(self, f):
#         def wrapper():
#             for i in range(self.num):
#                 f()
#
#         return wrapper
#
#
#
# @Repeter(5)
# def foo():
#     print('foo')
#
# foo()
# Создайте приложение по выпечке пиццы. Каждая
# пицца содержит разные компоненты. Используя механизм
# декораторов создайте разные пиццы:
# ■ Маргарита;
# ■ Четыре сыра;
# ■ Капричоза;
# ■ Гавайская.
#
# class Pizza1:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args):
#         print("Name: Margherita\nIngredients: basil, mozzarella, tomato")
#         return self.func(*args)
# class Pizza2:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args):
#         print("Name: Four Cheeses\nIngredients: 4 cheeses")
#         return self.func(*args)
# class Pizza3:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args):
#         print("Name: Camprichosa\nIngredients: mushroom...")
#         return self.func(*args)
# class Pizza4:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args):
#         print("Name: Hawaiian\nIngredients: ananas")
#         return self.func(*args)
# def orderPizza(q):
#     print(f"{q} pizza ordered")
#     ls = [Pizza1, Pizza2, Pizza3, Pizza4]
#     answer = int(input("Enter choose(1,2,3,4): "))
#     @ls[answer-1]
#     def bakePizza():
#         print("Pizza is baking...")
#     bakePizza()
# orderPizza(4)

#  Property
# class Student:
#   def __init__(self, name):
#       self.__name = name
#
#   @property #get_name
#   def name(self):
#       return self.__name
#
#   @name.setter
#   def name(self, value):
#       self.__name = value
#
#   @name.deleter  # property-name.deleter decorator
#   def name(self):
#       print('Deleting..')
#       del self.__name

# class Point3D:
#  def __init__(self, x, y, z):
#     self.x = x
#     self.y = y
#     self.z = z
#
#  @classmethod
#  def verify_coord(cls, coord):
#     if type(coord) != int:
#        raise TypeError("Координата должна быть целым числом")
#
#  @property
#  def x(self):
#     return self._x
#
#  @x.setter
#  def x(self, coord):
#     self.verify_coord(coord)
#     self._x = coord
#
#  @property
#  def y(self):
#     return self._y
#
#  @y.setter
#  def y(self, coord):
#     self.verify_coord(coord)
#     self._y = coord
#
#  @property
#  def z(self):
#     return self._z
#
#  @z.setter
#  def z(self, coord):
#     self.verify_coord(coord)
#     self._z = coord





# Descritpor
# class Number:
#     def __set_name__(self, owner, variable):
#         self.variable = "_" + variable
#     @classmethod
#     def check_number(cls, value):
#         if type(value) != int:
#             raise TypeError("Error type data")
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.variable]
#     #           Point3d.__dict[Number._x]
#     def __set__(self, instance, value):
#         print(f"__set__: {self.variable} = {value}")
#         instance.__dict__[self.variable] = value
# #       pt1(Point3D)._x = 1
# class Point3D:
#     x = Number() # x._x
#     y = Number()
#     z = Number()
#     def __init__(self, x, y, z):
#         self.x = x #x._x
#         self.y = y #y._y
#         self.z = z
#
# pt1 = Point3D(1, 2, 3)
# pt2 = Point3D('1', 2, 3)
# print(pt2.x)
#
# import  this
# class Number:
#     max_number = 0
#     min_number = 10
#
#     def method1(self):
#         print(self.__dict__)
#
# n = Number()
# n.method1()
#
# # type(name_class,typle of base classes,dict of fields,dict of methods)
# P = type('Point',(),{'x':10, 'y':0})
# p = P()
# print(p.x)


# class A:
#     instanse = None
#     def __new__(cls,x):
#         if cls.instanse is not None:
#             return  cls.instanse
#         else:
#             cls.instanse = super().__new__(cls)
#             return  cls.instanse
#
#
#     def __init__(self,x):
#         self.x = x
#         print('Object created!')
#
#     def __str__(self):
#         return  f'DATA[{self.x}]'
#
# a = A(5)
# a1 = A(10)
#
# print(a.x, a1.x)
# from typing import Protocol, runtime_checkable
# @runtime_checkable
# class Item(Protocol):
#     name: str
#     age: int
#
# class Person:
#     def  __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# class Employee(Person):
#     def  __init__(self,position,salary,name,age):
#         super().__init__(name,age)
#         self.position = position
#         self.salary = salary
#
#
# def show_persons(persons):
#     for i in persons:
#         if isinstance(i, Item):
#             print(f'{i.name}, {i.age}')
#         else:
#             print('Unkown Person')
#
# persons = [Person('Name1',10),Person('Name2',20),Person('Name3',30),Employee('HR',1000,'Employer1',40)]
# show_persons(persons)



#   @property #get_name
#   def name(self):
#       return self.__name
#
#   @name.setter
#   def name(self, value):
#       self.__name = value
#
#   @name.deleter  # property-name.deleter decorator
#   def name(self):
#       print('Deleting..')
#       del self.__name

import json
import os

ADMIN_FILE_DIRECTORY = 'admin_file'
USERS_FILE_DIRECTORY = 'users_file'
TESTS_FILE_DIRECTORY = 'tests_file'

class Person:

    def __init__(self,login,password):
        self._login = login
        self._password = password

        @property
        def login(self):
            return self._login

        @login.setter
        def login(self,value):
            self._login = value

        @login.deleter
        def login(self):
            del self._login

        @property
        def password(self):
            return  self._password

        @password.setter
        def password(self,value):
            self._password = value

        @password.deleter
        def password(self):
            del self._password

class User(Person):

    def __init__(self,login,password,first_name,last_name,address,tel):
        super().__init__(login,password)
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.tel = tel

class Admin(Person):

    def __init__(self,login,password):
        super().__init__(login,password)


def loading_toJSON(value,directory):
    try:
        with open(f'{directory}.json','w') as write_file:
            json.dump(value,write_file)
    except  Exception as e:
        print(f'Error: {str(e)}')

def unloading_toJSON(directory):
    try:
        with open(f'{directory}.json', "r") as read_file:
            return json.load(read_file)
    except  Exception as e:
        print(f'Error: {str(e)}')




admin_data = unloading_toJSON(ADMIN_FILE_DIRECTORY)
# print(admin_data['admin'][])

print('who are you?\n1.User\n2.Admin\n3.Exit')
c = int(input('Choose: '))

while c != 3:
    if c == 2:

        if not os.path.isfile(f'{ADMIN_FILE_DIRECTORY}.json'):
            admin = Admin('', '')
            print('it\'s you first entrance')
            admin._login = input('please write login: ')
            admin._password = input('please write password: ')
            loading_toJSON({'login': str(hashlib.md5(admin._login.encode('ascii')).digest()),
                            'password':str(hashlib.md5(admin._password.encode('ascii')).digest())},ADMIN_FILE_DIRECTORY)
        else:
            #TODO 'admin has already been created
            print('Pleace, enter login and password')
            l,p = [hashlib.md5(input('Enter login: ').encode('ascii')).digest(),
                   hashlib.md5(input('Enter password: ').encode('ascii')).digest()]
            if admin_data['login'] == str(l) and admin_data['password'] == str(p):

                print('Welcom admin')
            else:
                print('not')

    c = int(input('Choose: '))




