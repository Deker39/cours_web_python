from abc import ABC,abstractmethod

class IProtoType(ABC):
    @staticmethod
    @abstractmethod
    def clone():
        """clone obj"""

class Product(IProtoType):

    def __init__(self,f):
        self.field = f

    def clone(self):
        #   Product(data)
        return type(self)(self.field)


obj1 = Product('prod1')
obj2 = obj1
print(f'obj1: {obj1}')
print(f'obj1: {obj2}')
obj1 = Product('prod1')
obj2 = obj1.clone()
print(f'obj1: {obj1}')
print(f'obj1: {obj2}')