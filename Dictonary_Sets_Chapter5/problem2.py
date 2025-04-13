# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).

'''
# Method1
s = set() # Creating a empty set
for i in range(1,9):
    num=int(input(f"Enter {i} Number:"))
    s.add(num)
print(s)
'''


# Method2
s = set()

num=input("Enter Number:")
s.add(int(num))
num=input("Enter Number:")
s.add(int(num))
num=input("Enter Number:")
s.add(int(num))
num=input("Enter Number:")
s.add(int(num))
num=input("Enter Number:")
s.add(int(num))
num=input("Enter Number:")
s.add(int(num))
num=input("Enter Number:")
s.add(int(num))

print(s)
