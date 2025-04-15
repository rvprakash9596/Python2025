# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company="Microsoft"

    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p1 = Programmer("RaviPrakash",55000,226201)
print(p1.name,p1.company,p1.salary,p1.pin)

p2 = Programmer("Saurabh",65000,226201)
print(p2.name,p2.company,p2.salary,p2.pin)

p3 = Programmer("Vidya",85000,276201)
print(p3.name,p3.company,p3.salary,p3.pin)

p4 = Programmer("Kumkum",89000,286201)
print(p4.name,p4.company,p4.salary,p4.pin)