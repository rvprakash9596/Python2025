# 4. Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a=[1,54,55,45,80,120,700,550,545788785,0]
f=list(filter(divisible5,a))
print(f)
