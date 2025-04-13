# 8. If languages of two friends are same; what will happen to the program in problem 6?
# ans= values can be same for different keys but keys can't same for different values


dict = {} # empty dictonary

for i in range(1,4):
    name=input("Enter friends name:")
    lang=input("Enter your favourite Language:")
    dict.update({name:lang})
print(dict)

