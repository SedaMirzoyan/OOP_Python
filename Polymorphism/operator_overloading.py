#Operator overloading

class Complex_Number:
    """    
    This is a class for all complex numbers, 
    with overloaded __add__ and __sub__ magic methods

    Attributes:
        real (int): real part of complex number
        imaginary (int): imaginary part of complex number
    """
    def __init__(self, r, i):
        """
        Initializes a Complex number instance.

        Args:
            r (int): real part of complex number
            i (int): imaginary part of complex number
        """
        self.real = r
        self.imaginary = i


    def __add__(self, other):
        """
        Calculate sum of imaginary parts, then sum of real parts,
        convert them into string and return in a formatted way
        """
        return str(self.real + other.real) + " + " + str(self.imaginary + other.imaginary) + "i"
    

    def __sub__(self, other):
        """
        Calculate subtraction of imaginary parts, then subtraction of real parts,
        convert them into string and return in a formatted way
        """
        return str(self.real - other.real) + " + " + str(self.imaginary - other.imaginary) + "i"



"""
create 2 complex number objects, add then subtract numbers
"""
cn1 = Complex_Number(2, 3)
cn2 = Complex_Number(5, 9)
print(cn1 + cn2)
print(cn2 - cn1)