# FUNCTIONS WITH ARGUMENTS
# A function can accept some value it can work with. We can put these values in the
# parentheses.
# A function can also return value as shown below:

#Function with argument
def greet(name):
    print("Good Day ! , "+name)
greet("Ravi Prakash")
greet("Saurabh")


#Function with ending concept
def greet(name,ending):
    print("Good Day! , "+name)
    print(ending)
greet("Ravi Prakash","Thank You!")
greet("Saurabh","How are You?")


#Function with 'return' concept
def goodDay(name,ending):
    print("Good Day"+name)
    print(ending)
    return "ok"
a=goodDay("Harry","Thank You")
print(a)

