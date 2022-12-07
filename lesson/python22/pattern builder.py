from abc import ABC,abstractmethod

class IBulder(ABC):

    @staticmethod
    @abstractmethod
    def build_a():
        "creat product a"

    @staticmethod
    @abstractmethod
    def build_b():
        "creat product b"

    @staticmethod
    @abstractmethod
    def build_c():
        "creat product c"


    @staticmethod
    @abstractmethod
    def get_result():
        "return final product"

class Product():
    def __init__(self):
        self.parts = []

class Builder(IBulder):

    def __init__(self):
        self.product = Product()

    def build_a(self):
        self.product.parts.append('a')
        return  self

    def build_b(self):
        self.product.parts.append('b')
        return self

    def build_c(self):
        self.product.parts.append('c')
        return self

    def get_result(self):
        return  self.product

class Director:

    @staticmethod
    def construct():
        return  Builder().build_a().build_b().build_c().get_result()


product = Director.construct()
print(product.parts)