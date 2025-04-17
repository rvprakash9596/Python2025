# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

l=[10,54,55,45,78,14,36,42,46,47]

for i,item in enumerate(l):
    if i==2 or i==4 or i==6:
        print(item)


