'''__INIT__() CONSTRUCTOR
__init__() is a special method which is first run as soon as the object is created.
__init__() method is also known as constructor.
It takes ‘self’ argument and can also take further arguments.'''

class Employee:
    language="Java"
    salary=500000

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an Object Here") # dunder method which is automatically called

    def getInfo(self):
        print(f"Language = {self.language} , Salary={self.salary}")

    @staticmethod
    def greet():
        print("Good Morning!")


obj1=Employee("Saurabh",550000,"JavaScript")
print(obj1.name,obj1.salary,obj1.language)

# obj1.name="Ravi Prakash"
# print(obj1.name,obj1.salary)

obj1.getInfo()

# obj3=Employee()
# obj3.greet()  # hm is greet method ko kisi bhi object me pass kr sakte hainn