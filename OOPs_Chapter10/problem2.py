# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator :
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The Square is {self.n*self.n}")
    def cube(self):
        print(f"The Cube = {self.n*self.n*self.n}")
    def sqrt(self):
        print(f"Square Root = {self.n**1/2}")

a = Calculator(8)
a.square()

a.cube()

a.sqrt()

