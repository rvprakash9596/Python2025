class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        super().__init__() # this will access the method of its parent class that is Employee
        print("Constructor of Programmer")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c=3

# obj=Employee()
# print(obj.a)


# o=Programmer()
# print(o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)