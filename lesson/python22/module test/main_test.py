import requests


# class SimpleCalc:
#     def sum(self,a,b):
#         if isinstance(a,int) and isinstance(b,int):
#             return a + b
#         else:
#             return  'error'
#
#     def substract(self,a,b):
#         if isinstance(a,int) and isinstance(b,int):
#             return a - b
#         else:
#             return  'error'
#
#     def mult(self,a,b):
#         if isinstance(a,int) and isinstance(b,int):
#             return a * b
#         else:
#             return  'error'
#
#     def divide(self,a,b):
#         if b == 0:
#             raise  ZeroDivisionError('Errrr')
#         if isinstance(a,int) and isinstance(b,int):
#             return a / b
#         else:
#             return  'error'
#
# class Character:
#
#     def __init__(self, name):
#         self.name = name
#
#
#     def character(self):
#         response = requests.get(' https://rickandmortyapi.com/api/character/2')
#         return  response.json()

#
# sc = SimpleCalc()
# print(sc.sum(5,5))
# print(sc.mult(10,5))
# print(sc.substract(2,2))
# print(sc.divide(5,5))

class FirstSimpleClass:

    def __init__(self, arr: set):
        self._arr = arr

    def sum_set(self):
        return  sum({i for i in self._arr})

    def avg_set(self):
        return  sum({i for i in self._arr})/len(self._arr)

    def max_set(self):
        return max(self._arr)

    def min_set(self):
        return min(self._arr)


class SecondSimpleClass:

    def __init__(self,value = None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value,int):
            self._value = value
        else:
            raise 'error'

    def  convert_value_to_octal_system(self):
        return  oct(self._value)

    def  convert_value_to_hexadecimal_system(self):
        return hex(self._value)

    def  convert_value_to_binary_system(self):
        return bin(self._value)


# ssc = SecondSimpleClass(10)
# ssc.value = '10'
# print(ssc.convert_value_to_binary_system())
# print(ssc.convert_value_to_octal_system())
# print(ssc.convert_value_to_hexadecimal_system())