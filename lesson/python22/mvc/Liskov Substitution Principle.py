from abc import ABC

# Принцип подстановки Барбары Лисков
class Feline(ABC):
    def mewo(self) -> None:
        print('Error not impl')

class Cat(Feline):
    def mewo(self) -> None:
        print('Meow')

class Tiger(Feline):
    def mewo(self) -> None:
        print('Rrrrr')