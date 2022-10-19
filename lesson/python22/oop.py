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


class Human:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f'{self.name}')

class Worker:
    def __init__(self,salary):
        self.salary = salary
    def show(self):
        print(f'{self.salary}')


class Employee(Human,Worker):
    def __init__(self,name,salary):
        Human.__init__(self,name)
        Worker.__init__(self,salary)


    # def show(self):
    #     print(f'{self.name}, {self.salary}')



p1 = Employee('den',200)

Worker.show(p1)
Human.show(p1)