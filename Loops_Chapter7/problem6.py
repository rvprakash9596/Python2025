# 6. Write a program to calculate the factorial of a given number using for loop.

N=int(input("Enter The Number : "))
product=1
for i in range(1,N+1):
    product=product*i
print(f"The Factorial of {N} = {product}")
