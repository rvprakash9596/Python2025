# THE GLOBAL KEYWORD
# ‘global’ keyword is used to modify the variable outside of the current scope.

a=89 # its the global variable

def fun():
    # global a
    a=3
    print(a)

# a=89
fun() # yaha pr 3 print hoga
print(a) # yaha pr 89 jo ki global variable hai wo print hoga
