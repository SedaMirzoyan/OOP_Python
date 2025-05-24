#Hybrid inheritance

class A:
    def display(self):
        print("display from A")

class B(A):
    def display(self):
        print("display from B")


class C:
    def show(self):
        print("show from C")


class D(B, C):
    def display(self):
        print("display from D")

    def show(self):
        print("show from D")    


d = D()
d.show()
d.display()
print(D.mro())