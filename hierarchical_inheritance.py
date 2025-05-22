#Hierarchical inheritance

class Animal:
    def __init__(self, num_heart):
        self.num_heart = num_heart

    def sleep(self):
        print("I can sleep")

    def eat(self):
        print("I can eat")


class Mammal(Animal):
    def __init__(self, num_heart, name, color):
        super().__init__(num_heart)
        print("I am mammal")
        self.name = name
        self.color = color

    def run(self):
        print("I can run")


class Fish(Animal):
    def __init__(self, species):
        print("I am fish")
        self.species = species

    def swim(self):
        print("I can swim")


class Amphibian(Animal):
    def __init__(self, num_heart, species):
        print("I am amphibian")
        Animal.__init__(self, num_heart)
        self.species = species


    def jump(self):
        print("I can jump")



mammal = Mammal(1, "Teo", "beige")
mammal.run()
print(mammal.num_heart)
amphibian = Amphibian(1, "frog")
print(amphibian.species)
fish = Fish("salmon")
print(fish.species)
