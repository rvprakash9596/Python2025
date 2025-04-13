''' A built-in data type that stores set of values marks = [87, 64, 33, 95, 76]
    It can store elements of different types (integer, float, string, etc.)
    List is mutable means ki list k data ko hm change kr sakte hain.
'''

friends=["Ravi",9839029547,23,27.25,"Prakash"]
print(friends)
print(friends[1])

friends[2]="Grapes" # unlike String lists are mutable mtlb changable hoti hai
print(friends) # ['Ravi', 9839029547, 'Grapes', 27.25, 'Prakash']

#List Indexing
print(friends[1:4])
print(friends[0:])
print(len(friends))






