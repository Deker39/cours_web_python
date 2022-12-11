from abc import ABC,abstractmethod

class IShape(ABC):

    @staticmethod
    @abstractmethod
    def draw():
        pass

class IShapeImpl(ABC):

    @staticmethod
    @abstractmethod
    def draw_impl():
        pass


class CircleImpl(IShapeImpl):

    @staticmethod
    def draw_impl():
        print('Circle')

class SquareImpl(IShapeImpl):

    @staticmethod
    def draw_impl():
        print('Square')

class Circle(IShape):

    def __init__(self,impl):
        self.impl = impl()

    def draw(self):
        self.impl.draw_impl()


class Square(IShape):

    def __init__(self, impl):
        self.impl = impl()

    def draw(self):
        self.impl.draw_impl()

circle = Circle(CircleImpl)
square = Square(SquareImpl)

circle.draw()
square.draw()