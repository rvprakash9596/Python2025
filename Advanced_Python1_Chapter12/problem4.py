# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

try:
    a=int(input("Enter 1st Number:"))
    b=int(input("Enter 2nd Number:"))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")
