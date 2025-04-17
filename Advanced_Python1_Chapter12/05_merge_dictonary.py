# DICTIONARY MERGE & UPDATE OPERATORS
# New operators | and |= allow for merging and updating dictionaries.



dict1={101:"Ravi",102:"Saurabh"}
dict2={103:"Ritik",104:"Duggu"}

merged = dict1 | dict2

print(f"After Merging ={merged}")