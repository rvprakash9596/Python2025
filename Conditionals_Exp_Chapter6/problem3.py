#3. A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe ", “click ". Write a program to detect these spams.

p1="Make a lot of money"
p2="buy now"
p3="subscribe "
p4="click "

message = input("Enter your message : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This message is Spam")
else:
    print("Comment is not Spam")

