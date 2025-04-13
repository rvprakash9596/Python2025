# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list=[1,2,1]

copy_l1=list.copy()

copy_l1.reverse()

if(list==copy_l1):
    print(list," is palindrome")
else:
    print(list," is not palindrome")