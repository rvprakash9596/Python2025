# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator :
    def __init__(self,n):
        self.n=n
    
    @staticmethod
    def hello():
        print("Hello Ji! Good Morning")

    def square(self):
        print(f"The Square is {self.n*self.n}")
    def cube(self):
        print(f"The Cube = {self.n*self.n*self.n}")
    def sqrt(self):
        print(f"Square Root = {self.n**1/2}")

a = Calculator(8)
a.hello()
a.square()

a.cube()

a.sqrt()
