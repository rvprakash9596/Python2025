# 1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a=10
b=200
c=25
print(f"Greatest Value is {greatest(a,b,c)}")