# 7. If the names of 2 friends are same; what will happen to the program in problem 6?

dict = {} # empty dictonary

for i in range(1,4):
    name=input("Enter friends name:")
    lang=input("Enter your favourite Language:")
    dict.update({name:lang})
print(dict)


# dict does not allowed duplicate keys , if it occurs then it updates
