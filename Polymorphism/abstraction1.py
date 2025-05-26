#Abstract class and abstract method

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, n, color):
        self.num_of_wheels = n
        self.color = color


    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def __init__(self, color):
        self.num_of_wheels = 4
        self.color = color

    def drive(self):
        print("Driving car")


class Bike(Vehicle):
    def __init__(self, color):
        self.num_of_wheels = 2
        self.color = color

    def drive(self):
        print("Driving bike")


class Scooter(Vehicle):
    # def __init__(self, color):
    #    self.num_of_wheels = 2
    #    self.color = color

    def drive(self):
        print("Driving scooter")


scooter = Scooter(2, "red")
print(scooter.color)

car = Car("blue")
print(car.num_of_wheels)








