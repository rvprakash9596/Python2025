# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''
Dear <|Name|>,
You are Selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Ravi Prakash") .replace("<|Date|>","17 April 2025")) # isko chaining bolte hain




