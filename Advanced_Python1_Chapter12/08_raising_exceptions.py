a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))

if(b==0):
    raise ZeroDivisionError("Our program is not div by Zero")
else:
    print(f"The division a/b is {a/b}")