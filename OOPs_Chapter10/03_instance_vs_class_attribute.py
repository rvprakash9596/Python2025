# Note: Instance attributes, take preference over class attributes during assignment & retrieval

class Employee:
    language="Python" # This is is class attribute
    salary=1200000

obj1 = Employee()

# Note: Instance attributes, take preference over class attributes during assignment & retrieval
# obj1.language="Java" 
print(obj1.language,obj1.salary) 




