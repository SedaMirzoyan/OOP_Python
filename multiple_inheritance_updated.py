#Multiple inheritancs

class LandAnimal:
    """
    This is base class for all land animals.
    """
    def __init__(self, name):
        """
        Initializes a land animal instance.

        Args:
            name (string): name of the land animal
        """
        self.name = name
        self.num_eyes = 2
        self.num_nose = 1


    def walk(self):
        """
        Prints message in walk method
        """
        print("I can walk")


    def swim(self):
        """
        Prints message in swim method
        """
        print("I am a Land Animal, I can swim")



class WaterAnimal:
    """
    This is base class for all water animals.
    """
    def __init__(self, heart):
        """
        Initializes a water animal instance.

        Args:
            heart (string): number of heart
        """
        self.num_tail = 1
        self.num_heart = heart
    

    def swim(self):
        """
        Prints message in swim method
        """
        print("I am a Water Animal, I can swim")



class Amphibian(LandAnimal, WaterAnimal):
    """
    Amphibian class inherits from both Land Animal and Water Animal classes
    """
    def __init__(self, name, heart):
        """
        Initializes amphibian instance.
        Calling Wzter Animal and Land Animal constructors as well.

        Args:
            name (string): name of the land animal
            heart (string): number of heart
        """
        WaterAnimal.__init__(self, heart)
        LandAnimal.__init__(self, name)


    def sleep(self):
        """
        Prints message in sleep method
        """
        print("I can sleep")


    def swim(self):
        """
        Prints message in swim method, overrides base classes methods
        """
        print("I can live in both land and water, I can swim")


    def display(self):
        """
        Prints attributes in display method
        """
        print(f"I am {self.name} I can swim and sleep")



"""
Create amphibian object, with name and number of heart,
calling swim, sleep methods, print number of heart and eyes attributes 
"""
ob = Amphibian("Frog", 1)
ob.swim()
ob.sleep()
#print(Amphibian.mro())
#print(ob.num_tail)
print(ob.num_heart)
print(ob.num_eyes)

print("calling Water Animal's swim method")
WaterAnimal.swim(ob)
print("calling Land Animal's swim method")
LandAnimal.swim(ob)
ob.display()
