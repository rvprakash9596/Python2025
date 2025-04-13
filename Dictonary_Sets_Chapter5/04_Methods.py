# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# Method	            Description	                Example	                    Output
# A.union(B)	        All unique elements	        `A	                            B`
# A.intersection(B)	    Common elements	            A & B	                    {3, 4}
# A.difference(B)	    In A not in B	            A - B	                    {1, 2}
# A.symmetric_difference(B)	Elements in A or B but not both	A ^ B	{1, 2, 5, 6}

set1={1,5,30,6,5,5,4,4,5,"Ravi",25.25}
print(set1)

set1.add(27)
print(set1)
print(set1,type(set1))

set1.update([20,22,22.23])
print(set1)

print(set1.remove(20))
print(set1)

print(set1.discard(20)) # Removes 20 if present; no error if not
print(set1)


set2= set1.copy()
print(set2,set2.add(47))

s={1,5,4,6}
print(s)
popped = s.pop() # Removes & returns a random element
print("Popped value is ",popped)
print("Remaining Set is :",s)



