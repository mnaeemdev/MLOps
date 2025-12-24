# Practicing the concept of self argument in Python OOP
# The self parameter in Python is a reference to the current instance of the class.
# It is used to access variables and methods associated with the current object.
# When a method is called on an object, Python automatically passes the object as the first argument to the method.
# This is why we use 'self' to refer to instance variables and methods within the class.

class Person:
    def __init__(self):
        print("Person Object Created")
        print(id(self))  # Prints the unique ID of the object
        self.name = "Alice"
        self.age = 30

    def work(self, job):
        print(f"{self.name} is working as a {job}.")

person1 = Person()
print(id(person1))  # Prints the unique ID of person1

person1.work("Data Scientist")
print("Person Name:", person1.name)

person1.sex = "Male"  # Dynamically adding an attribute to the object
print("Person Sex:", person1.sex)