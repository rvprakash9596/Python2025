# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.


from random import randint
class Train:
    def __init__(sel,trainNo):
        sel.trainNo=trainNo
    def book(ravi,fro,to):
        print(f"Ticket is booked in Train no : {ravi.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train No : {self.trainNo} is running on time")
    def getFare(self,fro,to):
        print(f"Ticket fare in Train No {self.trainNo} from {fro} to {to} is {randint(110,135)}")
t = Train(15032)
t.book("Lucknow","Khalilabad")
t.getStatus()
t.getFare("Lucknow","Khalilabad")
