# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.



# Method 1
'''
dict = {} # empty dictonary

for i in range(1,5):
    name=input("Enter friends name:")
    lang=input("Enter your favourite Language:")
    dict.update({name:lang})
print(dict)
'''

#Method 2

dict2={}
name=input("Enter friends name:")
lang=input("Enter your favourite Language:")
dict2.update({name:lang})

name=input("Enter friends name:")
lang=input("Enter your favourite Language:")
dict2.update({name:lang})

name=input("Enter friends name:")
lang=input("Enter your favourite Language:")
dict2.update({name:lang})

name=input("Enter friends name:")
lang=input("Enter your favourite Language:")
dict2.update({name:lang})


print(dict2)
