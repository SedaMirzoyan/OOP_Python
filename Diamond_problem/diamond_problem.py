#diamond problem

class A:
    """
    Base A class, with display and show methods,
    which prints generic message
    """
    def display(self):
        print("display from A")

    def show(self):
        print("show from class A")


class B(A):
    """
    B class derived from A class
    """

    def display(self):
        """
        Prints generic message, overrides base display method
        """
        print("display from B")


    def show(self):
        """
        Prints generic message, overrides base show method
        """
        print("show from class B")    


class C(A):
    """
    C class derived from A class
    """
    def display(self):
        """
        Prints generic message, overrides base display method
        """
        print("display from C")


    def show(self):
        """
        Prints generic message, overrides base show method
        """
        print("show from class C")


class D(B, C):
    """
    D class derived from both B and C classes
    """
    #def display(self):
    #    print("display from D")
    
    def show(self):
        """
        calling C class's show method        
        """
        #super().show()  #this one is calling B show method
        C.show(self)



#create object of D class
d = D()

#B class's display will be called
d.display()
print(D.mro())

#C class display will be called
d.show()