#Operator overloading

class Complex_Number:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    
    def __add__(self, other):
        return str(self.real + other.real) + " + " + str(self.imaginary + other.imaginary) + "i"
    
    def __sub__(self, other):
        return str(self.real - other.real) + " + " + str(self.imaginary - other.imaginary) + "i"


cn1 = Complex_Number(2, 3)
cn2 = Complex_Number(5, 9)
print(cn1 + cn2)
print(cn2 - cn1)