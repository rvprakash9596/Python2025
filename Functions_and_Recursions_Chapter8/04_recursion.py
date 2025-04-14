# Recursion is a function which calls itself.It is used to directly use a mathematical formula as function.

# Factorial is the precise example of Recursion

'''
factorial(0)= 1
factorial(1)= 1
factorial(2)= 2 X 1
factorial(3)= 3 X 2 X 1
factorial(4)= 4 X 3 X 2 X 1
factorial(5)= 5 X 4 X 3 X 2 X 1

factorial(n)= n X n-1 X n-2 X .......3 X 2 X 1

factorial(n)= n* factorial(n-1)
'''

def fact(n):
    if(n==0 or n==1):
        return 1
    return n * fact(n-1)
n=int(input("Enter Number : "))
print(f"The factorial of {n} = {fact(n)}")

print(fact(5))
print(fact(6))
print(fact(7))
print(fact(0))
print(fact(1))


'''
The programmer needs to be extremely careful while working with recursion to ensure
that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most
direct way to code an algorithm.
'''