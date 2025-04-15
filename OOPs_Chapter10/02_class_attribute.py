#Creating Class
class Employee:
    language="Python" # This is is class attribute
    salary=1200000

#creating object
obj1 = Employee()

obj2=Employee()


#printing objects
obj1.name="Ravi Prakash" # This is a is instance / object attribute
print(obj1.name,obj1.language,obj1.salary) 

obj2.name="Saurabh Kumar"
print(obj2.name,obj2.language,obj2.salary)

# Here name is instance(object) attribute and salary , language are class attributes as they are directly belong to the class.


