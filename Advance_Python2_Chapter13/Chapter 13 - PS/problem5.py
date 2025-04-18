# 5. Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

list=[1,54,55,45,80,120,700,550,545,0,788,785,47821]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,list))




# print(max(list))