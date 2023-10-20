from uuid import uuid4


class User:

    """
    This class is made to register users
    """
    __users_dictionery = {}

    def __init__(self, username: str, password: str, phone_number=None) -> str | None:
        """
        Initializing an instance of the User class
        """
        self.__password = password
        self.phone_number = phone_number
        self.id = str(uuid4())
        self.username = username


    @staticmethod
    def username_is_exsist(username: str):
        if username in User.__users_dictionery:
            return True
        return False


    @staticmethod
    def password_is_valid(password: str):   
        if len(password) >= 4:
            return True
        return False    
        
 #-----------------------------------------------------------key = "1"-----------------------------------------------------------#

    @classmethod
    def sign_up(cls, username: str, password: str, phone_number:str = None):

        """
       This function is a classmethod and registers the user in the 
       user class after receiving the information
        """

        if not cls.username_is_exsist(username):
            if cls.password_is_valid(password): 
                new_user_account = cls(username, password, phone_number)
                cls.__users_dictionery[username] = new_user_account
            else:
                raise ValueError("Enter at least four characters for password")
        else:
            raise ValueError("This username already exists. try again") 

#-----------------------------------------------------------key = "2"-----------------------------------------------------------#


    @classmethod
    def sign_in(cls, username: str, password: str):

        """
        This function checks the condition that the username be unique
        And  ntered a valid password that belongs to the user we are entering.
        """
        
        if cls.username_is_exsist(username):
            if cls.__users_dictionery[username].__password == password:
                return cls.__users_dictionery[username]
            raise ValueError("Invalid password. try again...")
        raise ValueError("The username is not correct. try again")   



#-----------------------------------------------------------key = "2-1"-----------------------------------------------------------#

    def __str__(self) -> str:
        """
        This function use to show user
        information in the special format
        """
        return f"name: {self.username}, id: {self.id}, phone number: {self.phone_number}"


#-----------------------------------------------------------key = "2-2"-----------------------------------------------------------#
    @classmethod
    def change_username_and_phone_number(cls ,username: str, new_username: str, new_phone_number: str = None):

        """
        This function changes the username and phone number
        """  
        if not cls.username_is_exsist(new_username):
            cls.__users_dictionery[new_username] = cls.__users_dictionery.pop(username)
            cls.__users_dictionery[new_username].username = new_username
            cls.__users_dictionery[new_username].phone_number = new_phone_number
            username = new_username
        else:
            raise ValueError("This username already exists. try again")    
 
#-----------------------------------------------------------key = "2-3"-----------------------------------------------------------#
 

    @staticmethod
    def valid_new_password(new_password: str, repeat_new_password: str):

        """
        This function cheack the new password
        and repeated new password is equal toghether
        """
        if new_password == repeat_new_password:
            return True
        raise ValueError("new password and repeated new password is not equal toghether")   
    

    @classmethod
    def update_password(cls, old_password: str, username: str, new_password: str):

        """
        Replacing the new password with the previous password of a user
        """
        if cls.__users_dictionery[username].__password == old_password:
            if cls.password_is_valid(new_password):
                cls.__users_dictionery[username].__password = new_password
            else:
                raise ValueError("Enter at least four characters for password")  
        raise ValueError("Invalid password. try again...")        


     