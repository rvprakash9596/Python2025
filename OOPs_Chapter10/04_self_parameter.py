class Student:
    branch="CSE"
    fee=94904
    college="IET LKO"

    def getInfo(self):
        print(f"Branch is {self.branch} , Fee is {self.fee}  , College is {self.college}")
    def greet(self):
        print("Good Morning")

std1=Student()
std1.language="Mech Engg." # This is instance attribute
# print(std1.branch,std1.fee,std1.college)

# std1.getInfo() ya to ye likho ya neeche wala liko , dono same hi hai

std1.greet()
Student.getInfo(std1)
