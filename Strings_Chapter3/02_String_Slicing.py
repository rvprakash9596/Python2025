# String slicing is used for getting a part of the string

str="Maharashtra"
print(len(str))

print(str[2])
print(str[1])
print(str[0:2])
print(str[0:])
print(str[:11])

name="raviprakash4344"
nameshort=name[0:5]
print(nameshort)
nameshort=name[0:5]



name2="harry"
print(name2[0:3])
print(name2[-4:-1])
print(name2[1:4]) # ye barabar hai iske name2[-4:-1]


str3='''namakisgood'''
print(len(str3))
print(str3[-7:-3]) # or 
print(str3[4:8])



# Slicing with skip value

a='0123456789'
print(a[1:7:3])

a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(a[1:9])
print(a[1:9:4])


