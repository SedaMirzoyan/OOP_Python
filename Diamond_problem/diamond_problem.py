#diamond problem

class A:
    def display(self):
        print("display from A")

    def show(self):
        print("show from class A")


class B(A):
    def display(self):
        print("display from B")

    def show(self):
        print("show from class B")    

class C(A):
    def display(self):
        print("display from C")

    def show(self):
        print("show from class C")

class D(B, C):
    #def display(self):
    #    print("display from D")
    
    def show(self):
        #super().show()  #this one is calling B show method
        C.show(self)

d = D()
d.display()
print(D.mro())
d.show()