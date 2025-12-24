from advance import BankAccount

# Creating an instance of BankAccount
account1 = BankAccount()
print("Account Owner:", account1.owner)
print("Account Type:", account1.account_type)

# print("Initial Balance:", account1.__balance) # This will raise an AttributeError
print("Initail Balance:", account1._BankAccount__balance)  # Accessing private attribute using name mangling

account1._BankAccount__balance = 100  # Modifying private attribute using name mangling
print("Updated Balance:", account1._BankAccount__balance)  # Accessing updated private attribute

#Using Setter method to modify private attribute
account1.set_balance(500)

# Using Getter and Setter methods to access and modify private attributes
print("Balance using Getter:", account1.get_balance())



