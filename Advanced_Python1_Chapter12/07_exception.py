try:
    a=int(input("Enter a number :"))
    print(a)

except ValueError as v:
    print("Heyyy")
    print(v)
    
except Exception as e:
    print("Aapko sirf integer number enter krnaa hai chacha",e)

print("Thank You for using Exception Handling Topic")