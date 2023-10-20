from users import User


def receive_information(key):

    """
    This function receive users information
    including username password and phone number
    when the key value is "1" and return them
    """
    if key == 1:
        username = input("username: ")
        password = input("password: ")
        phone_number = input("phone number(optional): ")
 
        if phone_number == "":
            phone_number = None
        return  username, password, phone_number 
    elif key == 2:
        username = input("username: ")
        password = input("password: ")
        return  username, password
    elif key == 2-2:
        new_username = input("new username: ")   
        new_phone_number = input("new phone number: ") 
        if new_phone_number == "":
            new_phone_number = None
        return  new_username, new_phone_number
    elif  key == 2-3:
        old_password = input("old_password: ")
        new_password = input("new password: ") 
        repeat_new_password = input("repeat new password: ") 
        return  old_password, new_password, repeat_new_password 


while True:
    try:
        key = input("According to the requested operation,"
        " enter one of the following options:\n"
        "---------------------------------------\n"
        "To exit the user registering program:  Enter number 0\n"
        "---------------------------------------\n"    
        "Start the user registering program: Enter number 1\n"
        "---------------------------------------\n"    
        "Entering to registering users and Edit its information : Enter number 2\n"
        "---------------------------------------\n"    
        "key:")
        if key == "0":
            break
        elif key == "1":

            username, password, phone_number = receive_information(1)
            User.sign_up(username, password, phone_number)

        elif key == "2":  
            username, password = receive_information(2)
            if User.sign_in(username, password):
                while True:
                    key = input("According to the requested operation,"
                    " enter one of the following options:\n"
                    "---------------------------------------\n"
                    "To print all information:  Enter number 1\n"
                    "---------------------------------------\n"    
                    "Edit username and phone number: Enter number 2\n"
                    "---------------------------------------\n" 
                    "Edit password: Enter number 3\n"
                    "---------------------------------------\n"  
                    "Sign out of the user account: Enter number 4\n"
                    "---------------------------------------\n"    
                    "key:")
                
                    if key == "1":
                        print(User.sign_in(username, password))
                    if key == "2":
                        new_username, new_phone_number = receive_information(2-2)
                        User.change_username_and_phone_number(username, new_username, new_phone_number)
                        username = new_username
                    if key == "3":
                        old_password, new_password, repeat_new_password = receive_information(2-3)
                        if User.valid_new_password(new_password, repeat_new_password):
                            User.update_password(old_password, username, new_password)
                        
                        else:
                            continue    

                    if key == "4":  
                        break 
    except ValueError as e:
        if('Enter at least four characters for password' in str(e)):
            print("Enter at least four characters for password")
        if('This username already exists. try again' in str(e)):
            print("This username already exists. try again")
        if('Invalid password. try again...' in str(e)):
            print("Invalid password. try again...")
        if('The username is not correct. try again' in str(e)):
            print("The username is not correct. try again")   
        if('new password and repeated new password is not equal toghether' in str(e)):
            print("new password and repeated new password is not equal toghether")                      
    finally:
        continue 
