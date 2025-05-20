#Multilevel inheritance

class Animal:
    def __init__(self, num_heart):
        print("Animal constructor")
        self.num_heart = num_heart

    def sleep(self):
        print("I am an animal, I can sleep")

    def eat(self):
        print("I am an animal, I can eat")

class Mammal(Animal):
    def __init__(self, name):
        print("Mammal constructor")
        self.name = name

    def run(self):
        print("I am mammal, I can run")

    def eat(self):
        #super().eat()
        print("I am mammal, I can eat")

class Lion(Mammal):
    def __init__(self, color, name, num_heart):
        print("Lion constructor")
        Mammal.__init__(self, name)
        Animal.__init__(self, num_heart)
        self.color = color

    def hunt(self):
        print("I am lion, I can hunt")

    def eat(self):
        super().eat()
        Animal.eat(self)
        print("I am lion, I can eat")


lion = Lion("beige", "Simba", 1)
lion.eat()
print(lion.name)
