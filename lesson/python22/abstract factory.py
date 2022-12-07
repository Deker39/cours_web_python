# abstract factory
from abc import ABC,abstractmethod

# class AbctractCar(ABC):
#
#     @abstractmethod
#     def get_body_type(self):
#         pass
#
# class SedanCar(AbctractCar):
#
#     def __init__(self):
#         self.body = 'sedan'
#
#     def get_body_type(self):
#         return f'Body type: {self.body}'
#
#
# class HetchbackCar(AbctractCar):
#
#     def __init__(self):
#         self.body = 'hetchback'
#
#     def get_body_type(self):
#         return f'Body type: {self.body}'
#
#
# class PickupCar(AbctractCar):
#
#     def __init__(self):
#         self.body = 'pickup'
#
#     def get_body_type(self):
#         return f'Body type: {self.body}'
#
#
# class CarFactory():
#     @staticmethod
#     def build_car(type):
#         try:
#             if type == 'sedan':
#                 return  SedanCar()
#             elif type == 'hetchback':
#                 return  HetchbackCar()
#             elif type == 'pickup':
#                 return PickupCar()
#             raise AssertionError('Type is not valid')
#         except AssertionError as e:
#             print(e)
#
# list_type = ['sedan','pickup','sedan','hetchback','jeep']
#
# for t in list_type:
#     car = CarFactory.build_car(t)
#     body = car.get_body_type()
#     print(body)

class CarFactory(ABC):
    @abstractmethod
    def get_body_type(self):
        """return a body type"""

    @abstractmethod
    def get_hardware(self):
       pass

class Body(ABC):

    @abstractmethod
    def assembly_engine(self):
        """engine type"""

    @abstractmethod
    def body_type(self):
        """body type"""

class Hardware(ABC):

    @abstractmethod
    def put_conlose(self):
        """engine type"""

    @abstractmethod
    def assembly_seats(self):
        """body type"""

class RegularBody(Body):

    def assembly_engine(self):
        print('Hatchback')

    def body_type(self):
        print('1.2 Motor')


class SportBody(Body):

    def assembly_engine(self):
        print('Sedan')

    def body_type(self):
        print('2.0 Motor')


class SandartHardware(Hardware):

    def put_conlose(self):
        print('Small Screen with gigital speedometr')

    def assembly_seats(self):
        print('normal fabric')

class LuxaryHardware(Hardware):

    def put_conlose(self):
        print('Big Screen with Analog speedometr')

    def assembly_seats(self):
        print('leather fabric')


class FamilyCar(CarFactory):

    def get_body_type(self):
        return RegularBody()

    def get_hardware(self):
        return SandartHardware()

class OutdoorCar(CarFactory):

    def get_body_type(self):
        return SportBody()

    def get_hardware(self):
        return SandartHardware()

class BachelorCar(CarFactory):

    def get_body_type(self):
        return RegularBody()

    def get_hardware(self):
        return LuxaryHardware()

class WalthyCar(CarFactory):

    def get_body_type(self):
        return SportBody()

    def get_hardware(self):
        return LuxaryHardware()



def prepare_order(customer):
    # if customer == 'Family':
    #     body = RegularBody()
    #     hard = SandartHardware()
    factories = {
        'Family': FamilyCar(),
        'Outdoor': OutdoorCar(),
        'Beachelr': BachelorCar(),
        'Wealthy': WalthyCar()
    }

    car = factories[customer]

    body = car.get_body_type()
    hard = car.get_hardware()

    body.assembly_engine()
    body.body_type()
    hard.assembly_seats()
    hard.put_conlose()


prepare_order('Family')