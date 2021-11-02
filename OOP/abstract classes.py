# prevents a user from creating an object of that class
# compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration ut does not have an implementation

from abc import ABC, abstractmethod
# ABC = Abstract Base Class

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print('Driving the car')
    def stop(self):
        print('Car stopped')

class Motorcycle(Vehicle):
    def go(self):
        print('Riding the motorcycle')
    def stop(self):
        print('Bike stopped')

# can't create an object of abstract class
# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()