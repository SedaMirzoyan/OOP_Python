#Multiple inheritancs

class Mammal:
    def __init__(self, name):
        self.name = name
        self.num_eyes = 2
        self.num_nose = 1

    def walk(self):
        print("I can walk")

    def swim(self):
        print("I am a mammal, I can swim")


class Reptile:
    def __init__(self, heart):
        self.num_tail = 1
        self.num_heart = heart

    def crawl(self):
        print("I can crawl")
    
    def swim(self):
        print("I am a reptile, I can swim")


class Platypus(Mammal, Reptile):
    def __init__(self, name, heart):
        Reptile.__init__(self, heart)
        Mammal.__init__(self, name)

    def sleep(self):
        print("I can sleep")

    def swim(self):
        print("I am both mammal and reptile, I can swim")

    def display(self):
        print(f"I am {self.name} I can swim, sleep and crawl")


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
