# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:
# "The name of the student is RaviPrakash , his marks are 85 in CN and phone number is 9839029547"

name=input("Enter your name : ")
marks = int(input("Enter your Marks in Computer Network : "))
phone = int(input("Enter Phone Number :"))

a = f"The name of the student is {name} , his marks are {marks} in CN and phone number is {phone}".format(name,marks,phone)

print(a)