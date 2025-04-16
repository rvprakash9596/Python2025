class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3

obj=Employee()
print(obj.a) # prints the attribute of a 

# print(obj.b) # Employee' object has no attribute 'b'

o=Programmer()
print(o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)