# 1. Encapsulation, Inheritance, and Polymorphism in Python OOP
# 2. Getter and Setter methods to access and modify private attributes
# 3. Static Methods


# Encapsulation in Python OOP

class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute
        self.__account_number = "123456789"  # Private attribute
        self.owner = "John Doe"  # Public attribute
        self.account_type = "Savings"  # Public attribute
        # self.menu()
    
    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method for balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount. Balance cannot be negative.")

