myList=[1,2,9,7,8,9,10]

'''squaredList=[]
for item in myList:
    squaredList.append(item*item)

#same work can be done using LIST COMPREHENSIONS in one line    
'''

squareList = [i*i for i in myList]
print(squareList)