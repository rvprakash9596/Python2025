# 1. Write a program to print multiplication table of a given number using for loop.
tbl=int(input("Enter number to print table of :"))
for i in range(1,11):
    print(f"{tbl} * {i} =",tbl*i)