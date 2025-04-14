# 1. Write a program to print multiplication table of a given number using while loop.

tbl=int(input("Enter number to printt table of : "))
i=1
while(i<=10):
    print(f"{tbl} * {i}=",tbl*i)
    i=i+1
