# The ‘enumerate’ function adds counter to an iterable and returns it

l=[10,54,55,45,78]

'''index=0
for item in l:
    print(f"The item number at index {index} is {item}")
    index +=1
    
yahi same work hm enumerate se kr sakte han
'''

for index,item in enumerate(l):
    print(f"The item number at index {index} is {item}")


print("Done!")