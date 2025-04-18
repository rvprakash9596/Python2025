from functools import reduce

# map() : Map applies a function to all the items in an input_list.

l = [1,2,3,4,5]

square = lambda x : x*x

sqList = map(square,l)
print(list(sqList))


# filter() : Filter creates a list of items for which the function returns true.

def even(n):
    if (n%2 == 0):
        return True
    return False
onlyEven = filter(even, l) # filter() method takes two parameters
print(list(onlyEven))

# reduce() : Reduce applies a rolling computation to sequential pair of elements.

def sum(a,b):
    return a+b
print(reduce(sum,l))

mul = lambda x,y: x*y
print(reduce(mul,l))
