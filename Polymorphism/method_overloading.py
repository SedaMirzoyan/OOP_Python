#Method overloading

class A:
    def add(self, a, b, c=0):
        return a + b + c
    
    def mul(self, *args):
        product = 1
        for i in args:
            product = product * i
        return product
    


a = A()
print(a.add(5, 6))
print(a.add(5, 6, 7))

print(a.mul(1, 2, 3, 4, 5))
print(a.mul(12, 34))