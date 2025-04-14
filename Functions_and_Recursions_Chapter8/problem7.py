# 7. Write a python function to remove a given word from a list ad strip it at the same time.
def rem(list,word):
    n=[]
    for item in list:
        if not(item==word):
            n.append(item.strip(word))
    return n
list=["Ravi","Rohan","Sonu","an"]
print(rem(list,"an"))

