#login Authentication

userid="RaviPrakash4344"
password="Ravi@12345"
print("*********Login Here**********")
print("="*50)
uid=input(("Please enter your userid : "))#ram
pwd=input(("Please enter your password : "))#123
if(uid==userid and pwd==password):
    print("")
    print("*"*30)
    print("You Are Login Successfully . ")
    print("*"*30)
else:
    #if(userid!=uid)
    print("Wrong Userid or Password . ")
    print("*"*30)