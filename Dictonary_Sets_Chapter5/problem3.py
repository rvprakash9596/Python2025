# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

#Method1
set1 = {18,'18'}
print(set1)


#Method2
s=set()
s.add(18)
s.add("18")
print(s)

