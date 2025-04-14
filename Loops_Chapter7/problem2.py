# 2. Write a program to greet all the person names stored in a list ‘list’ and which starts with S. list= ["Harry", "Soham", "Sachin", "Rahul"]

list= ["Harry", "Soham", "Sachin", "Rahul"]
for name in list:
    if(name.startswith("S")):
        print(f"Welcome {name}")