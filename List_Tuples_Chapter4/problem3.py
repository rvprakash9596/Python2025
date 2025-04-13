# 3. Check that a tuple type cannot be changed in python.

tpl=(2,"raviprakash4344",23.56)
print(len(tpl))
print(tpl)

tpl[0]="ID"
print(tpl) # TypeError: 'tuple' object does not support item assignment