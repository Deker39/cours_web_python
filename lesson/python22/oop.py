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

class Human:

    def __init__(self,full_name,bd,phone,city,country,address):
        self.__full_name = full_name
        self.__bd = bd
        self.__phone = phone
        self.__city = city
        self.__country = country
        self.__address = address

    def info(self):
        return f'{self.__full_name},{self.__bd},{self.__phone},{self.__city},{self.__country},{self.__address}'

    def __str__(self):
        return f'{self.__full_name},{self.__bd},{self.__phone},{self.__city},{self.__country},{self.__address}'

    def get__full_name(self):
        return  "Name " + self.__full_name

    def set__full_name(self,fname):
        if isinstance(fname,str) and 3 < len(fname) < 30:
            self.__full_name = fname
        else:
             raise  ValueError(f'{fname} id wrong data...')



h1 = Human('NOone','22.22.22','+124124124','Lviv','Ukraine','adders')
print(h1)
h1.set__full_name('Alex')
print(h1)
