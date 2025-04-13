# 1. Write a program to find the greatest of four numbers entered by the user.

'''
#Method1
num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))
num3=int(input("Enter Number 3: "))
num4=int(input("Enter Number 4: "))

if(num1>num2 and num1>num3 and num1>num4):
    print(num1," is greatest")
elif(num2>num1 and num2>num3 and num2>num4):
    print(num2," is greatest")
elif(num3>num1 and num3>num2 and num3>num4):
    print(num3," is greatest")
else:
    print(num4," is greatest")
'''



'''
#Method 2
numbers = []
num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))
num3=int(input("Enter Number 3: "))
num4=int(input("Enter Number 4: "))
numbers.append(num1)
numbers.append(num2)
numbers.append(num3)
numbers.append(num4)
print("You have entered number :",numbers)
greatest = max(numbers)
print("Greatest number = ",greatest)
'''


'''
#Method3 using max() method
numbers = []
for i in range(1,5):
    num=int(input(f"Enter Number {i} :"))
    numbers.append(num)
print("You have entered Numbers : ",numbers)

greatest=max(numbers)
print("The greatest number is = ",greatest)
'''



