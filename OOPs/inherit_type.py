# Practicing the types of Inheritance in Python OOP

# ***********Single Inheritance************

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display_info(self):
#         print(f"Vehicle Brand: {self.brand}, Model: {self.model}")

# class Car(Vehicle):  # Child class inheriting from Vehicle
#     def __init__(self, brand, model, year):
#         super().__init__(brand, model)  # Calling the parent class constructor
#         self.year = year

#     def display_info(self):  # Overriding the display_info method
#         print(f"Car Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# my_car = Car("Toyota", "Camry", 2020)
# my_car.display_info()



# ***********Multiple Inheritance************
# class Grandparent:
#     def __init__(self):
#         self.grandparent_first_name = "Pervaiz"
#         self.grandparent_last_name = "Qasim"
#     def grandparent_method(self):
#         print(f"Grandparent Name: {self.grandparent_first_name} {self.grandparent_last_name}")

# class Parent(Grandparent):
#     def __init__(self):
#         super().__init__()
#         self.parent_first_name = "Naeem"
#         self.parent_last_name = self.grandparent_first_name
#     def parent_method(self):
#         print(f"Parent Name: {self.parent_first_name} {self.parent_last_name}")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.child_first_name = "Muhammad"
#         self.child_last_name = "-Bin- " + self.parent_first_name
#     def child_method(self):
#         print(f"Child Name: {self.child_first_name} {self.child_last_name}")

# child = Child()
# child.grandparent_method()
# child.parent_method()
# child.child_method()


# ***********Hierarchical Inheritance************ 
# class Parent:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"Hello, I am {self.name}.")

# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is studying.")

# child1 = Child1("Alice")
# child1.greet()
# child1.play()

# child2 = Child2("Bob")
# child2.greet()  
# child2.study()
        

# ***********Multilevel Inheritance - Diamond Problem************
# class A:
#     def show(self):
#         print("Class A method called.")

# class B(A):
#     def show(self):
#         print("Class B method called.")
#         super().show()  # Calling method from class A

# class C(A):
#     def show(self):
#         print("Class C method called.")
#         super().show()  # Calling method from class A

# class D(B, C):
#     def show(self):
#         print("Class D method called.")
#         super().show()  # This will follow the MRO

# d = D()
# d.show()
# print("Method Resolution Order:", D.mro())
# # In this example, class D inherits from both B and C, which in turn inherit from A. When we call the show method on an instance of D, Python follows the Method Resolution Order (MRO) to determine which method to execute first. 
# # The output demonstrates how Python resolves the method calls in the presence of multiple inheritance, effectively handling the diamond problem.


# # ***********Hybrid Inheritance************
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} created.")
    def sound(self):
        print(f"Animal {self.name} is making a sound.")
    
class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color
        print(f"Mammal {self.name} with fur color {self.fur_color} created.")
    def feed(self):
        print(f"Mammal {self.name} is feeding its babies.")

class Bird(Animal):
    def fly(self):
        print(f"Bird {self.name} is flying.")
    
class Bat(Mammal, Bird):
    def __init__(self, name, fur_color):
        Mammal.__init__(self, name, fur_color) # Calling Mammal's constructor explicitly
        print(f"Bat {self.name} created.")
    def sound(self):
        print(f"Bat {self.name} is screeching.")
    

bat = Bat("Bruce", "Black")
bat.sound()  # Overridden method from Bat class