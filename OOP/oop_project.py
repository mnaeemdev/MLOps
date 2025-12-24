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
                pass
                # self.message_friends()
            elif choice == '4':
                pass
                # self.write_post()
            else:  
                print("Exiting ChatBook. Goodbye!")
                break


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



# Creating an instance of the chatbook class to run the program
obj = chatbook()