# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint
class Train:

    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in Train no : {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train No : {self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f"Ticket fare in Train No {self.trainNo} from {fro} to {to} is {randint(110,135)}")


t = Train(15032)
t.book("Lucknow","Khalilabad")
t.getStatus()
t.getFare("Lucknow","Khalilabad")
