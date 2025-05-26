#Duck typing

class Dog:
    def swim(self):
        print("Dog is swimming")

    def voice(self):
        print("I am Dog")

class Duck:
    def swim(self):
        print("Duck is swimming")

    def voice(self):
        print("I am Duck")


class Fish:
    def swim(self):
        print("Fish is swimming")

    def voice(self):
        print("I am Fish")


def display(obj):
    obj.voice()
    obj.swim()



dog = Dog()
display(dog)
fish = Fish()
display(fish)
duck = Duck()
display(duck)
