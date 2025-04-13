# There are following Set Operations 

# Union                     A.union(B)
# Intersection              A.intersection(B)
# Difference                A.difference(B)
# Symmetric Difference	    A.symmetric_difference(B)
# Subset	                A.issubset(B)
# Superset	                A.issuperset(B)
# Disjoint	                A.isdisjoint(B)

A={1,45,6,7}
B={6,45,7,8,1,78}

#Union
print(f"{A} U {B} =",A.union(B))

#Intersection
print(A.intersection(B))

#Difference
print(A.difference(B))


#Symmetric Difference
print(A.symmetric_difference(B)) # {6, 8, 45, 78} mtlb jo dono me common hai usko nhi print krega

#Subset
print(A.issubset(B)) # True

#Superset
print(A.issuperset(B))

#Disjoint
print(A.isdisjoint(B))



