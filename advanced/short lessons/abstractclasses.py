from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):  # A method to be used for more than one thing (printing car instead of motorcycle),
        pass       # required to be overridden in the child class.

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print('The car started')

    def stop(self):
        print('The car stopped')


class Motorcycle(Vehicle):

    def go(self):
        print('The motorcycle started')

    def stop(self):
        print('The motorcycle stopped')


motorcycle = Motorcycle()
car = Car()

car.go()
car.stop()

motorcycle.go()
motorcycle.stop()
