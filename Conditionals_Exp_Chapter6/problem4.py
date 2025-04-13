# 4. Write a program to find whether a given username contains less than 10 characters or not.

user_name=input("Enter User Name : ")

if(len(user_name)<10):
    print("UserName contains less than 10 Characters")
else:
    print("UserName contains greater than or equal to 10 Characters")
