marks=int(input("Enter your marks : "))

if(marks<=0):
    print("Fail")
elif(marks>=1 and marks<=33):
    print("C")
elif(marks>=34 and marks<=60):
    print("B")
elif(marks>=61 and marks<=90):
    print("A")
else:
    print("Excellent")


print("End of program")