#Multilevel inheritance

class Animal:
    def sleep(self):
        print("I am an animal, I can sleep")

    def eat(self):
        print("I am an animal, I can eat")

class Mammal(Animal):
    def run(self):
        print("I am mammal, I can run")

    def eat(self):
        #super().eat()
        print("I am mammal, I can eat")

class Lion(Mammal):
    def hunt(self):
        print("I am lion, I can hunt")

    def eat(self):
        super().eat()
        print("I am lion, I can eat")


lion = Lion()
lion.eat()