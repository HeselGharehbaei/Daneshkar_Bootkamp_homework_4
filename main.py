from users import User
while True:
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

        username, password, phone_number = User.getting_information()  
        User.do_register(username, password, phone_number)
        
    elif key == "2":  
        username, password = User.getting_information_for_entering_to_user_account()
        if User.check_validation_of_username_and_password(username, password):
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
                    User.show_registeried_users(username)
                if key == "2":
                    new_username, new_phone_number = User.getting_new_information_for_changing_user_account()
                    User.username_phone_number_editator(username, new_username, new_phone_number)
                if key == "3":
                    old_password, new_password, repeat_new_password = User.getting_information_for_entering_to_new_password_account()  
                    User.check_old_new_repeat_passwords_length_new_password(new_password)
                    User.check_old_new_repeat_passwords_length_old_password(old_password)
                    User.check_old_new_repeat_passwords_length_repeat_new_password(repeat_new_password)
                    User.check_password_is_correct(old_password, username)
                    User.valid_new_password_and_repeat_new_password(new_password, repeat_new_password)
                    User.update_password(username, new_password) 
                if key == "4":  
                    break 





            
        # print(username, password,phone_number)    


