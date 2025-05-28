#Abstract class and abstract method

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    This is an abstract base class for all vehicles, 
    with drive abstract method
    """
    def __init__(self, n, color):
        """
        Initializes a Vehicle instance.

        Args:
            color (string): Color of the car
            n (int): number of the wheels
        """
        self.num_of_wheels = n
        self.color = color

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    """
    Represents a Car inherited from Vehicle class

    Attributes:
        color (string): Color of the car
        num_of_wheels (int): Number of wheels of the car
    """

    def __init__(self, color):
        """
        Initializes a Car instance.

        Args:
            color (string): Color of the car
        """
        self.num_of_wheels = 4
        self.color = color


    def drive(self):
        """
        Prints a generic message about car.
        """
        print("Driving car")


class Bike(Vehicle):
    """
    Represents a Bike inherited from Vehicle class

    Attributes:
        color (string): Color of the bike
        num_of_wheels (int): Number of wheels of the bike
    """

    def __init__(self, color):
        """
        Initializes a Bike instance.

        Args:
            color (string): Color of the bike
        """
        self.num_of_wheels = 2
        self.color = color

    def drive(self):
        """
        Prints a generic message about bike.
        """
        print("Driving bike")


class Scooter(Vehicle):
    """
    Represents a Scooter inherited from Vehicle class

    Attributes:
        color (string): Color of the scooter
        num_of_wheels (int): Number of wheels of the scooter
    """
    #def __init__(self, color):
    #    self.num_of_wheels = 2
    #    self.color = color

    def drive(self):
        """
        Prints a generic message about scooter.
        """
        print("Driving scooter")


"""
Calling Vehicle class constructor for creating scooter object, 
with number of wheels and color, then print scooter color
"""
scooter = Scooter(2, "red")
print(scooter.color)

"""
Create a car object with color attribute, then print number of wheels
"""
car = Car("blue")
print(car.num_of_wheels)








