#class Name:
    # ferld = ...

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

class Circle():

    def __init__(self,r):
        self.r = r

    def __add__(self, other):
        return self.r + other

    def __iadd__(self, other):
        self.r += other
        return  self.r

    def __sub__(self, other):
        self.r -= other
        return self.r

    def __isub__(self, other):
        return self.r - other

    def __eq__(self, other):
        return self.r == other
    def __lt__(self, other):
        return  self.r < other
    def __gt__(self, other):
        return  self.r > other
    def __le__(self, other):
        return  self.r <= other
    def __ge__(self, other):
        return  self.r >= other

o1 = Circle(5)
o2 = Circle(3)
print(o1+3)
print(o1-3)
o1 +=1
o2 -=2
print(o1)
print(o2)
print(o1==o2)
print(o1<o2)
print(o1>o2)
print(o1<=o2)
print(o1>=o2)

class Complex(object):

    def __init__(self, arg, static):
        self.arg = arg
        self.static = static
        # Formats our results
        print(self.arg + self.static)

    def __add__(self, other):
        return Complex(self.arg + other.arg, self.static + other.static)

    def __sub__(self, other):
        return Complex(self.arg - other.arg, self.static - other.static)

    def __mul__(self, other):
        return Complex((self.arg * other.arg) - (self.static * other.static),(self.static * other.arg) + (self.arg * other.static))

    def __truediv__(self, other):
        r = (other.arg ** 2 + other.static ** 2)
        return Complex((self.arg * other.arg - self.static * other.static) / r,(self.static * other.arg + self.arg * other.static) / r)

a1 = Complex(1, 5j)
a2 = Complex(6, 2j)

# Add
a1 + a2
# Subtract
a1 - a2
# Multiply
a1 * a2
# Divide
a1 / a2

