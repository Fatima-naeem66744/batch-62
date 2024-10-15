"""
Create a class Car with attributes like make, model, 
and year. Write methods to start the car and display its details.
 Then, create multiple instances of Car and
 use the methods on each instance.
"""

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} has started.") 
    def display(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
obj = Car("2005" , "5_c" , "2007")

obj.start()       
obj.display()       


"""
Design a base class Animal with a method speak(). Then, create two derived classes, Dog and
 Cat, that inherit from Animal. Override the speak() method in both derived classes to 
 make the Dog class print "Bark" and theCat class print "Meow". Create objects of both 
 Dog and Cat and call their speak() method.
"""

class Animal():
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")
class Cat(Animal):
    def speak(self):
        print("Cat meows.")
obj1 = Dog()
obj2 = Cat()

obj1.speak()

obj2.speak()




