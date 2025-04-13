marks={
    "Ravi":58,
    "Raju":87,
    "Duggu":77,
    101:["Duggu",34,87,45.36],
    0:"ram",
}


print(marks,type(marks))

# print(marks.items())# returns the all items of dictonary

# print(marks.keys())

# print(marks.values())

# print(marks.update({"Ravi":57,"101":["Dugggggguuuu"]}))

# print(marks)

# Both of not same
print(marks["Ravi"])
print(marks.get("Raju"))#
print(marks.get("Raju1"))# prints none,mtlb agar key iss name se nhi hai to none print krta hai get() method
#print(marks["Raju1"])# returns an error

print(marks.pop("Ravi")) # Returns 58 and removes 'Ravi'
print(marks)

print(marks.popitem()) # retuens last key and value & removes last key:value
print(marks)



# print(marks.clear())
# print(marks)






# Duplicate element "A" not allowed by Dictonary
dict ={
    "A":58,
    "B":87,
    "C":77,
    101:["D",34,87,45.36],
    0:"ram",
    "A":58
}
print(dict)

print(len(dict)) # 5 because A is written twice

print(len(marks))

