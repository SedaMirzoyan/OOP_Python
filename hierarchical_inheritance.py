#Hierarchical inheritance

class Animal:
    """
    Base class Animal
    """
    def __init__(self, num_heart):
        """
        Initializes an Animal instance.

        Args:
            num_heart (int): number_of heart of the animal
        """
        self.num_heart = num_heart


    def sleep(self):
        """
        Prints a generic message in sleep function.
        """
        print("I can sleep")


    def eat(self):
        """
        Prints a generic message in eat function.
        """
        print("I can eat")


class Mammal(Animal):
    """
    Mammal class, which inherits from Animal class
    """
    def __init__(self, num_heart, name, color):
        """
        Initializes Mammal instance.

        Args:
            num_heart (int): number_of heart of the animal
            name (string): name
            color (string): color

        Calling base class constructor as well with the help of super() function        
        """
        super().__init__(num_heart)
        print("I am a mammal")
        self.name = name
        self.color = color

    def run(self):
        """
        Prints a generic message in run function.
        """
        print("I can run")


class Fish(Animal):
    """
    Fish class, which inherits from Animal class
    """
    def __init__(self, species):
        """
        Initializes Fish instance.

        Args:
            species (string): species
        """
        print("I am fish")
        self.species = species

    def swim(self):
        """
        Prints a generic message in swim function.
        """
        print("I can swim")



class Amphibian(Animal):
    """
    Amphibian class, which inherits from Animal class
    """
    def __init__(self, num_heart, species):
        """
        Initializes Amphibian instance.

        Args:
            num_heart (int): number_of heart of the animal
            species (string): species

        Calling base class constructor as well with the help of super() function        
        """
        print("I am amphibian")
        Animal.__init__(self, num_heart)
        self.species = species


    def jump(self):
        """
        Prints a generic message in jump function.
        """
        print("I can jump")



"""
Create a mammal object with number_of_heart, name, color attributes,
call run method on it and print number of heart
"""
mammal = Mammal(1, "Teo", "beige")
mammal.run()
print(mammal.num_heart)

"""
Create a amphibian object with number_of_heart, species attributes,
and print species attribute
"""
amphibian = Amphibian(1, "frog")
print(amphibian.species)

"""
Create a fish object with species attribute,
and print species attribute
"""
fish = Fish("salmon")
print(fish.species)
