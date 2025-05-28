"""
Multiple inheritance example

Platypus is a mammal, but has mix of characteristics from reptiles, birds as well.
In the following example Platypus inherits from Mammal, Reptile and Bird classes.
"""

class Mammal:
    """
    This is base class for all mammals.
    """
    def __init__(self, name):
        """
        Initializes a Mammal instance.

        Args:
            name (string): name of the mammal
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
        print("I am a mammal, I can swim")



class Reptile:
    """
    This is base class for all reptiles.
    """
    def __init__(self, heart):
        """
        Initializes a Reptile instance.

        Args:
            heart (string): number of heart
        """
        self.num_tail = 1
        self.num_heart = heart


    def crawl(self):        
        """
        Prints message in crawl method
        """
        print("I can crawl")
    
    def swim(self):
        """
        Prints message in swim method
        """
        print("I am a reptile, I can swim")



class Bird:
    """
    This is base class for all birds.
    """
    def display(self):
        """
        Prints message in display method
        """
        print("I have a duck-like bill")



class Platypus(Mammal, Reptile, Bird):
    """
    Platypus class inhertits from Mammal, Reptile and Bird class
    """
    def __init__(self, name, heart):
        """
        Initializes a Reptile instance.

        Args:
            name (string): name of the platypus
            heart (string): number of heart
        """
        Reptile.__init__(self, heart)
        Mammal.__init__(self, name)


    def sleep(self):
        """
        Prints message in sleep method
        """
        print("I can sleep")


    def swim(self):
        """
        Prints message in swim method, overrides base method
        """
        print("I am both mammal and reptile, I can swim")


    def display(self):
        """
        Prints name in display method, calling base class display as well
        """
        super().display()
        print(f"I am {self.name} I can swim, sleep and crawl")



"""
Create platypus object, with name and number of heart,
calling swim, sleep methods, print number of heart and eyes attributes 
"""
ob = Platypus("Platypus", 1)
ob.swim()
ob.sleep()
#print(Platypus.mro())
#print(ob.num_tail)
print(ob.num_heart)
print(ob.num_eyes)


print("calling Reptile swim method")
Reptile.swim(ob)
print("calling Mammal swim method")
Mammal.swim(ob)
ob.display()


