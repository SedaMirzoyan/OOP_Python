#Hybrid inheritance

class A:
    """
    Base A class, which has display method.
    prints a generic message in display method.
    """
    def display(self):
        print("display from A")


class B(A):
    """
    Base B class, which has display method,
    prints a generic message in display method, overrides base method.
    """
    def display(self):
        print("display from B")


class C:
    """
    Base C class, which has display method,
    prints a generic message in display method.
    """
    def show(self):
        print("show from C")


class D(B, C):
    """
    D class, which inherits from both B and C classes
    """
    def display(self):
        """
        prints a generic message in display method, overrides base method.
        """
        print("display from D")


    def show(self):
        """
        prints a generic message in show method, overrides base method.
        """
        print("show from D")    



"""
create D class object, overrides show and display methods
"""
d = D()
d.show()
d.display()
print(D.mro())