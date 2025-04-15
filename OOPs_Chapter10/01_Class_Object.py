# Class: A class is a blueprint for creating object.
# Class name is written in pascal case

#OBJECT
'''
An object is an instantiation of a class. When class is defined, a template (info) is
defined. Memory is allocated only after object instantiation.
Objects of a given class can invoke the methods available to it without revealing the
implementation details to the user. – Abstractions & Encapsulation!

We identify the following in our problem.
• Noun → Class → Employee
• Adjective → Attributes → name, age, salary
• Verbs → Methods → getSalary(), increment()

'''


#Creating Class
class Employee:
    name="Ravi Prakash"
    language="Python"
    salary=1200000

#creating object
obj = Employee()

#printing objects
print("Name =",obj.name,obj.language,obj.salary)
