#Method overriding

class Animal:
    """
    This is base class for all animals, 
    with can_hunt class variable

    Attributes:
        num_heart (string): number of hearts
        name (string): name of the animal
    """
    can_hunt = True
    def __init__(self, num_heart, name):
        """
        Initializes a Vehicle instance.

        Args:
            num_heart (string): number of hearts
            name (string): name of the animal
        """
        print("Animal constructor")
        self.num_heart = num_heart
        self.name = name


    def sleep(self):
        """
        Prints a generic message in sleep method.
        """
        print("I am an animal, I can sleep")


    def eat(self):
        """
        Prints a generic message in eat method.
        """
        print("I am an animal, I can eat")
    


class Mammal(Animal):
    """
    Derived class Mammal class, which inherits from Animal class

    Attributes:
        name (string): name of the animal
    """
    def __init__(self, name):
        """
        Initializes a Mammal instance.

        Args:
            name (string): name of the mammal
        """
        print("Mammal constructor")
        self.name = name


    def run(self):
        """
        Prints a generic message in run method.
        """
        print("I am mammal, I can run")


    def eat(self):
        """
        Overrides base class eat method.
        """
        print("I am mammal, I can eat")



class Lion(Mammal):
    """
    Derived Lion class, which inherits from Mammal class

    Attributes:
        num_heart (string): number of hearts
        name (string): name of the animal
        color (string): color of the lion
    """
    def __init__(self, color, name, num_heart):
        """
        Initializes a Vehicle instance.

        Args:
            num_heart (string): number of hearts
            name (string): name of the animal
        """
        print("Lion constructor")
        Mammal.__init__(self, name)
        Animal.__init__(self, num_heart, name)
        self.color = color


    def hunt(self):
        """
        Print generic message in hunt method
        """
        print("I am lion, I can hunt")


    def eat(self):
        """
        Calling base class eat methods as well, and defining own eat method
        """
        super().eat()
        Animal.eat(self)
        print("I am lion, I can eat")


"""
Create lion object, call eat method and print Lion class attributes
"""
lion = Lion("beige", "Simba", 1)
lion.eat()
print(lion.name)
print(lion.can_hunt)
