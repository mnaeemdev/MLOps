from oop_project import chatbook

# Creating an instance of the chatbook class to run the program
user1 = chatbook()
print("User ID of first user:", user1.id)

chatbook.set_user_id(10)  # Setting user ID to 10 using static method
user2 = chatbook()
print("User ID of second user after setting to 10:", user2.id)