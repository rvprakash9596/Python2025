marks=int(input("Enter your marks : "))

# if Statement no 1
a=10
if(a%2==0):
    print("a is even")
# if Statement no 1


# if Statement no 2 
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
# if Statement no 2

print("End of program")