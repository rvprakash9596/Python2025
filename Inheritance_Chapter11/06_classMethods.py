# @classmethod is bound to the class not the object of the class.
# it uses cls not self
# cls mtlb ki wo class jis pr ye method chal rha hai


class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e=Employee()
e.a=45 # Object of the class
e.show() # The class attribute of a is 1 kyuki @classmethod is bound to the class not the object of the class.

