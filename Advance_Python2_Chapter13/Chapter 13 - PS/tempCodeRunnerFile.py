def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,list))