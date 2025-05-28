#Multiple inheritance

class LandAnimal:
    def __init__(self, name):
        self.name = name
        self.num_eyes = 2
        self.num_nose = 1

    def walk(self):
        print("I can walk")

    def swim(self):
        print("I am a Land Animal, I can swim")


class WaterAnimal:
    def __init__(self, heart):
        self.num_tail = 1
        self.num_heart = heart
    
    def swim(self):
        print("I am a Water Animal, I can swim")


class Amphibian(LandAnimal, WaterAnimal):
    def __init__(self, name, heart):
        WaterAnimal.__init__(self, heart)
        LandAnimal.__init__(self, name)

    def sleep(self):
        print("I can sleep")

    def swim(self):
        print("I can live in both land and water, I can swim")

    def display(self):
        print(f"I am {self.name} I can swim and sleep")


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
