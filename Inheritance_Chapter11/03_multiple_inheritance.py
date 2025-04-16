class Employee:
    company = "ITC"
    salary=550000
    name="Default Name"
    def show(self):
        print(f"The employee name is {self.name} and company is {self.company}")

class Coder:
    language="Python"
    def printLanguages(self):
        print(f"Out of all the language here is your language {self.language}")

class Programmer(Employee,Coder):
    company="Google Inc."
    def showLanguages(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


b=Programmer()

b.show()
b.printLanguages()
b.showLanguages()