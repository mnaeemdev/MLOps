# Practicing Inheritance in Python OOP

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")
    

class Dog(Animal):
    def speak(self):  # Overriding the speak method of the parent class
        print(f"{self.name} barks.")  # Using the name attribute from the parent class


class Parrot(Animal):
    def __init__(self, name, behavior):
        self.behavior = behavior
        super().__init__(name)  # Calling the parent class constructor
    def speak(self):  # Overriding the speak method of the parent class
        print(f"{self.name} chirps and he is very {self.behavior}")  # Using the name attribute from the parent class

parrot = Parrot("Sono","talkative")
parrot.speak()

animal = Animal("Generic Animal")
animal.speak()

dog = Dog("Buddy")
dog.speak()