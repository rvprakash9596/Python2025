# 4. Write a program to find whether a given number is prime or not.

n=int(input("Enter number to check Prime Or Not ? : "))
for i in range(2,n):
    if(n%i)==0:
        print(f"{n} is Not Prime.")
        break
else:
    print(f"{n} is Prime.")

