from abc import ABC,abstractmethod

class IA(ABC):

    @staticmethod
    @abstractmethod
    def method_a(self):
        pass


class IB(ABC):

    @staticmethod
    @abstractmethod
    def method_b(self):
        pass

class ClassA(IA):

    def method_a(self):
        print('method A')


class ClassB(IB):

    def method_b(self):
        print('method B')

class ClassBAdapter(IA):

    def __init__(self):
        self.b = ClassB()


    def method_a(self):
        self.b.method_b()

# items = [ClassA(),ClassB()]
#
# for items in items:
#     if isinstance(items,ClassB):
#         items.method_b()
#     else:
#         items.method_a()

items = [ClassA(),ClassBAdapter()]

for items in items:
    items.method_a()