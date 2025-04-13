
# list = [2, 1, 3]
# list.append(4) #adds one element at the end
# list.insert( idx, el ) #insert element at index
# list.sort( ) #sorts in ascending order
# list.reverse( ) #reverses list
# list.sort( reverse=True ) #sorts in descending order
# list.remove(1) #removes first occurrence of element
# list.pop(idx) # removes elements at idx

friends=["Ravi",9839029547,23,27.25,"Prakash"]
print(friends)
friends.append("SaurabhCaterersKhalilabad") # It will change the List , mtlb ye original list me value last me add karega
print(friends)

list=[2,1,47,20,0,4]
print(list)
print(list.sort()) # none hoga
print(list) # yaha pr final value sort hone k baad show karega

print(list.reverse())
print(list)
print(list.reverse())

l1=[1,10,3,56,8,2,4]
print(l1)

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(2, 47) # insert at 2nd index value = 47
print(l1)

print(l1.pop()) # returns last element
print(l1) # [56, 10, 47, 8, 4, 3, 2]

print(l1.pop(1))
print(l1)

print(l1.sort())
print(l1)

print(l1.remove(56))
print(l1)

l1.append(56)
print(l1)


l1.append(47)
print(l1)

l1.insert(2,9839029547)
print(l1)