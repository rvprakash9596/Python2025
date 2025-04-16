class Employee():
    company = "ITC"
    def show(self):
        print(f"The employee is {self.name} and salary is {self.salary}")

class Programmer(Employee):
    company="Google Inc."
    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language}")

a=Employee()
b=Programmer()

print(a.company,b.company)