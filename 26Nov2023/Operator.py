# Examples of python Operator's

'''x=20
y=10
z=3

print(x+y) #30
print(x-y) #10
print(x*y) #200
print(x%y) #0
print(x/y) #2.0
print(x/z) #6.666666666667
print(x//y)#2
print(x//z)#6


a=20.0
b=3
print(a/b) #6.666666666666667
print(a//b)#6.0
print(a//b)#6.0

c=20.0
d=6.0
print(c/d)  #3.3333333333333335
print(c//d) #3.0 bcz both operands are decimal

e=10
f=3
print(e/f)# 3.3333
print(e//f)# 3



#Exponent Examples
g=5
h=3
print(g*h) #15
print(g**h) #125 (5*5*5)


i="Ravi"
j="Prakash"
print(i**j) # this is invalid bcz exponent works only on numerical values 


1000.544 => floor=>1000   ceil=>1001
x=12.444  => 10
123.94444 => floor 123

'''

# x=10
# y=20
# print(x>y) #False
# print(10>50) #False
# print(2>=3) #False
# print(50>40) #True
# print(50>=40) #True
# print(50<40) #False
# print(50<=40) #False
# print(50<=50) #True
# print(10<20<30<50<20<60<=60>=10)#False
# #print(10==10>5>6>7<=7>6==6<==50)#False
# print(10==10>9>8>=7<=50)



# print(10==40)#false
# print(10==10)#True
# print(10!=10)#false


# print(10>10 and 30>40) #False
# print(10>20 and 20>50) #True
# print(True and True) #True
# print(True and False) #False
# print(False and false) #False
# print(False and False) # True
# print(False and True) #False



# print(True or True) #True
# print(True or False) #True
# print(False or False) # False
# print(False or True) #True
# print(False or False) #False

# print(not True) #False
# print(not False) #True
# print(not False) #True


# name="Ravi Prakash KLD"
# print("KLD" in name) #True
# print("KLD." in name) #False
# print("ravi." in name) #False
# print("ravi" in name) #False


"""name1="Techpile Technology Pvt. Ltd."
print("ECH" not in name1)#True
print("Technology" not in name1)#False
"""



# print("*"*50)

# x="Techpile Technology Pvt Ltd"

# a=input("Enter your message to find in collection : ")

# if(a in x):
    # print("Searches item is present in given collection .....")
# else:
    # print("Searches item is not present in given collection.....")
    



#==Assignment Operator==

# a=200.0
# b=3
# a//=b #a=a//b a=a/b 200.0//3=66.0
# print(a)


# x=20
# y=10

#x%=y
#print(x)

# x+=2 	#x=x+2		x=20+2=22
# print(x)

# x+=y	#x=x+y		x=x+y=20+10=30
# print(x)

# x1=2
# y1=4

# x1**=3   #x=x**3 x=2*2*2
# print(x1)

#x**=y #x=x**y   2*2*2*2=16

#Ternary Operator

x=20
y=30

print("Y IS BIG") if (y>x) else print("X is big")
print("Y IS BIG") if (y<x) else print("X IS LESS")
print(x," IS LESS") if (x<y) else print("X IS BIG")