from uuid import uuid4


class User:

    """
    This class is made to register users
    """
    users_list = {}

    def __init__(self, username: str, password: str, phone_number=None) -> str | None:
        """
        Initializing an instance of the User class
        """
        self.__password = password
        self.phone_number = phone_number
        self.id = str(uuid4())
        self.username = username


#-----------------------------------------------------------key = "1"-----------------------------------------------------------#

    @staticmethod
    def getting_information():

        """
        This function staticmethod inputs users information
        including username password and phone number
        when the key value is "1"
        """

        username = input("username: ")
        password = input("password: ")
        phone_number = input("phone_number(optional): ")
        if phone_number == '':
            phone_number = None
            return username, password, phone_number
        return username, password, phone_number


 


    @classmethod
    def do_register(cls, username: str, password: str, phone_number=None):

        """
       This function is a classmethod and registers the user in the 
       user class after receiving the information
        """


        if username in cls.users_list:
            print("This username already exists. try again")
            username = input("username: ")
            cls.do_register(username, password, phone_number=None)
        elif len(password) < 4:
            print("Enter at least four characters for password")
            password = input("password: ")
            cls.do_register(username, password, phone_number=None)
        new_registered_user_information = cls(username, password, phone_number)
        print(new_registered_user_information)
        cls.users_list[username] = new_registered_user_information
        print(cls.users_list)

    

#-----------------------------------------------------------key = "2"-----------------------------------------------------------#


    @staticmethod
    def getting_information_for_entering_to_user_account():

        """
        This function inputs information
        including username and password 
        when the key value is "2"
        """

        username = input("username: ")
        password = input("password: ")
        return username, password
 

    @classmethod
    def check_validation_of_username_and_password(cls, username: str, password: str):

        """
        This function checks the condition that the username be unique
        And  ntered a valid password that belongs to the user we are entering.
        """
        
        if username in cls.users_list:

            if cls.users_list[username].__password != password:
                print("The password is not correct. try again")
                password = input("password: ")
                cls.check_validation_of_username_and_password(username, password)
            elif  cls.users_list[username].__password == password: 
                return True  
        elif username  not in cls.users_list:
            print("The username is not correct. try again")
            username = input("username: ")
            cls.check_validation_of_username_and_password(username, password)  
        return True      



#-----------------------------------------------------------key = "2-1"-----------------------------------------------------------#

    def __str__(self) -> str:
        """
        This function use to show user
        information in the special format
        """
        return f"{self.username}: password: {self.__password}, id: {self.id}, phone number: {self.phone_number}"

    @classmethod
    def show_registeried_users(cls, username:str):
        """
        Due to the existence of __str__ function, 
        we can watch the created users by this function.
        """
        registered_user = cls.users_list[username]
        print(registered_user)
        

#-----------------------------------------------------------key = "2-2"-----------------------------------------------------------#
    @staticmethod
    def getting_new_information_for_changing_user_account():


        """
        This function inputs information
        including new username and password 
        when the key value is "2  >>  2"
        """

        new_username = input("new username: ")
        new_phone_number = input("new_phone_number: ")
        return new_username, new_phone_number

      

    @classmethod
    def username_phone_number_editator(cls, username:str, new_username: str, new_phone_number: str): 

        """
        This function changes the username and phone number
        """
        if new_username in cls.users_list:
            print("This username already exists. try again")
            new_username = input("new_username: ")
            cls. username_phone_number_editator(username, new_username, new_phone_number)
        if cls.is_usernamein_the_class_users_list(new_username):    
            cls.users_list[new_username] = cls.users_list.pop(username)
            cls.users_list[new_username].username = new_username
            cls.users_list[new_username].phone_number = new_phone_number
            cls.show_registeried_users(new_username)
            username = new_username
            print(cls.users_list)

#-----------------------------------------------------------key = "2-3"-----------------------------------------------------------#


    @staticmethod
    def getting_information_for_entering_to_new_password_account():

        """
        This function inputs information
        including new old_password and new_password and repeat_new_password
        when the key value is "2  >>  3"
        """

        old_password = input("olde_password: ")
        new_password = input("new_password: ")
        repeat_new_password = input("repeat_new_password: ")
        return old_password, new_password, repeat_new_password

                    
    @classmethod
    def check_old_new_repeat_passwords_length_old_password(cls, old_password:str):

        """
        This function checks the minimum length of the input password 
        """   

        if len(old_password) < 4:
            print("Enter at least four characters for password")
            old_password = input("old_password: ")
            cls.check_old_new_repeat_passwords_length_old_password(old_password)
        elif len(old_password) >= 4:
            return True 


                    
    @classmethod
    def check_old_new_repeat_passwords_length_new_password(cls, new_password:str):

        """
        This function checks the minimum length of the input password 
        """   

        if len(new_password) < 4:
            print("Enter at least four characters for password")
            new_password = input("new_password: ")
            cls.check_old_new_repeat_passwords_length_new_password(new_password)
        elif len(new_password) >= 4:
            return True             

    @classmethod
    def check_old_new_repeat_passwords_length_repeat_new_password(cls, repeat_new_password:str):

        """
        This function checks the minimum length of the input password 
        """   

        if len(repeat_new_password) < 4:
            print("Enter at least four characters for password")
            repeat_new_password = input("repeat_new_password: ")
            cls.check_old_new_repeat_passwords_length_repeat_new_password(repeat_new_password)
        elif len(repeat_new_password) >= 4:
            return True  


    @classmethod
    def check_password_is_correct(cls, old_password: str, username:str):  
        
        """
        Checking the correctness of the password   
        """

        if cls.users_list[username].__password !=  old_password:
            print("This password is not same to the user password try again: ")
            password = input("old_password: ")
            cls.check_password_is_correct(old_password, username )
        elif  cls.users_list[username].__password ==  old_password:   
            return True 

    @staticmethod
    def valid_new_password_and_repeat_new_password(new_password: str, repeat_new_password:str): 

        """
        Checking a new password and repeating it
        """

        if new_password != repeat_new_password:
            print("new_password and repeat_new_password is not same")
            repeat_new_password = input("repeat_new_password: ")
            new_password = input("new_password: ")
            cls.valid_new_password_and_repeat_new_password(new_password, repeat_new_password)
        elif new_password != repeat_new_password:    
            return True         

    @staticmethod
    def update_password(username, new_password):

        """
        Replacing the new password with the previous password of a user
        """
        User.users_list[username].__password = new_password




     