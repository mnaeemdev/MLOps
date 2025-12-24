##### ChatBook Social Media Application #####

class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def menu(self):  # Main menu method
        while True:
            print("Welcome to ChatBook!")
            print("1. Sign Up")
            print("2. Log/Sign In")
            print("3. Message to friends")
            print("4. Write a post")
            print("Press any other key to exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.sign_up()
            elif choice == '2':
                self.sign_in() 
            elif choice == '3':
                self.message_friends()
            elif choice == '4':
                self.write_post()
            else:  
                print("Exiting ChatBook. Goodbye!")
                break


    # Methods for sign up and sign in

    def sign_up(self):
        print("Sign Up")
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.username = username
        self.password = password
        print("Signed up successful!")
        print("\n")
        self.menu()

    def sign_in(self):
        print("Log In")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == self.username and password == self.password:
            self.logged_in = True
            print("Logged in successfully!")
        else:
            print("Invalid credentials. Please try again. / Not Signed up first. \nPlease Sign Up First.")
        print("\n")
        self.menu()

    # Methods for messaging friends and writing posts

    def message_friends(self):  
        if self.logged_in == True:
            friend_name = input("Enter your friend's name:")
            message = input("Enter your message:")
            print(f"Message sent to {friend_name}: \n{message}")
        else:
            print("Please log in to message friends.")
        print("\n")
        self.menu()

    def write_post(self):
        if self.logged_in == True:
            post_content = input("Write your post:")
            print("Post published:\n", post_content)
        else:
            print("Please log in to write a post.")
        print("\n")
        self.menu()


# Creating an instance of the chatbook class to run the program
obj = chatbook()