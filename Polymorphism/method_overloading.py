#Method overloading

class A:
    """
    class which has add and mul overloaded methods
    """
    def add(self, a, b, c=0):
        """
        Method overloading with the help of default argument c,
        we can call it with 2 or 3 arguments

        Args:
            a (int): a
            b (int): b
            c (int): c
        """
        return a + b + c
    
    
    def mul(self, *args):
        """
        Method overloading with the help of default *args,
        So we can pass any number of arguments

        Args:
            *args: any number of arguments
        """

        product = 1
        for i in args:
            product = product * i
        return product
    


"""
create an object of A class,
overloading with default argument for add method (for 2 or 3 arguments),
and with any number of arguments for mul method
"""
a = A()
print(a.add(5, 6))
print(a.add(5, 6, 7))

print(a.mul(1, 2, 3, 4, 5))
print(a.mul(12, 34))