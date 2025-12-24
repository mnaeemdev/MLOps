#Classes and Objects in Python
class Employee:
    def __init__(self): #Constructor to initialize object attributes
        print("Employee Object Created")
        self.id = 123
        self.name = "John Doe"
        self.salary = 5000000
        self.designation = "Software Engineer"

    def work(self, project): #Method to simulate work on a project
        print(f"{self.name} is working on {project}.")


emp = Employee()
print("Employee ID:", emp.id)
emp.work("AI Chatbot Development")


#Note: Everything in Python is a class object, including classes themselves
a = 10
str_obj = "Hello, World!"
lst = [1, 2, 3, 4, 5]
print(type(a))          # Output: <class 'int'>
print(type(str_obj))    # Output: <class 'str'>
print(type(lst))        # Output: <class 'list'>