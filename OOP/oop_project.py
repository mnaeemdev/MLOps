class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def menu(self):
        while True:
            print("Welcome to ChatBook!")
            print("1. Sign Up")
            print("2. Log In")
            print("3. Message to friends")
            print("4. Write a post")
            print("Press any other key to exit")
            choice = input("Choose an option: ")

            if choice == '1':
                pass
                # self.sign_up()
            elif choice == '2':
                pass
                # self.log_in()   
            elif choice == '3':
                pass
                # self.message_friends()
            elif choice == '4':
                pass
                # self.write_post()
            else:  
                print("Exiting ChatBook. Goodbye!")
                break

    
obj = chatbook() 
