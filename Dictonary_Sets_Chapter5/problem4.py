# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s= set()
s.add(45)
s.add(45.0)
s.add('45')

print(s)
print("The length of this set = ",len(s)) # The length of this set =  2


chk=1==1.0
print(chk) # yes True


print(1 == 1.0)         # True (values equal)
print(type(1))          # <class 'int'>
print(type(1.0))        # <class 'float'>
print(1 is 1.0)         # False (different objects & types)

set1={20,20.0,"20"}
print(len(set1))