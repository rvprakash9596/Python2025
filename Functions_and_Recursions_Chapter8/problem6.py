# 6. Write a python function which converts inches to cms.

def inch_to_cm(inch):
    return inch*2.54
    # 1 inch = 2.54 CM Hota hai
n=int(input("Enter Value In Inches : "))
print(f"The corresponding value in CM is {inch_to_cm(n)} CM")