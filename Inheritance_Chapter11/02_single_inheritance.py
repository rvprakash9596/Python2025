class Animal:
    def speak(self):
        print("Animal Can Speak ")

class Dog(Animal):
    def bark(self):
        print("Dog Barks at Strangers")
    
d = Dog()
d.bark()
d.speak()


