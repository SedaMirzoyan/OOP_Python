#Duck typing

class Dog:
    """
    Dog class with swim and voice methods,
    which print generic messages
    """
    def swim(self):
        print("Dog is swimming")

    def voice(self):
        print("I am Dog")


class Duck:
    """
    Duck class with swim and voice methods,
    which print generic messages
    """
    def swim(self):
        print("Duck is swimming")

    def voice(self):
        print("I am Duck")


class Fish:
    """
    Fish class with swim and voice methods,
    which print generic messages
    """
    def swim(self):
        print("Fish is swimming")

    def voice(self):
        print("I am Fish")


def display(obj):
    """
    This function does not care about actual type of an object,
    only that it has voice and swim methods

    Args:
        obj (class object): obj
    """
    obj.voice()
    obj.swim()



"""
create objects of dog, duck and fish classes and pass them to display function,
for each call it will print corresponding message
"""
dog = Dog()
display(dog)
fish = Fish()
display(fish)
duck = Duck()
display(duck)
