# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a=4 # a is class attribute of Demo

Obj=Demo()
print(Obj.a) #4 Prints class attribute because instance attribute is not present

Obj.a=0
print(Obj.a) #0 instance attribute is set

print(Demo.a)#4 prints the class attribute


