from classes import Credentials
from classes import User
import time, sys, random, getpass

def create_user(name,password):
    '''
    Function to create a user
    '''
    new_user = User(name,password)
    return new_user

def create_credentials(account_name,user_name,password):
    '''
    Function to create credentials
    '''
    new_credential = Credenetial(account_name,user_name,password)
    return new_credential

def delete_credential(credential):
    '''
    Function to delete credentials
    '''
    credential.delete_credential()

def save_credential(credential):
    '''
    Function to save credentials
    '''
    credential.save_credentials()

def find_credential(account):
    '''
    Function to find a credential using the account name
    '''
    return Credentials.find_by_account_name(account)    

def credential_exist(account):
    '''
    Function to check if a credential exists
    '''
    return Credentials.account_exists(account)

def display_credentials():
    '''
    Function to display the credentials
    '''
    return Credentials.display_credentials()

def copy_password(account):
    '''
    Function to copy password of the credentials password
    '''
    return Credentials.copy_password(account)

def main():

    time.sleep(1)
    print("Hello, Welcome to Password Locker, What is your name?")
    user_name = input()
    
    if user_name:
        print(f"\n Welcome {user_name},let me help you to create an account to use Password Locker \n")
    else:
        print("\n Weeelll, Since I don't know your name, let me call you User!!! Let us create an account then\n")

    print("--" * 80)
    login_name = input(">>> Enter the username you would like to use \n")
    login_password = getpass.getpass(">>> Enter the password you want to use \n")
    confirm_password = getpass.getpass(">>> Confirm your password \n")
    while True:
        if login_password != confirm_password:
            print("Passwords do not match!!")
            login_password = getpass.getpass(">>> Reenter the password  \n")
            confirm_password = getpass.getpass(">>> Reconfirm your password \n")
        else:
            print("Account Successfully created \n")
            break
    time.sleep(1)
    while True:
        login = input("Status: Logged Out \n Login to your account using the short code \lg\ or \login\ \n")
        if login == 'lg' or login.lower() == 'login':
            session_name = input("\n Username: ")
            session_pass = getpass.getpass("\n Password: ")
            print("Authenticating Credentials....")
            time.sleep(3)
            while True:
                if session_name != login_name or session_pass != login_password:
                    print("--"*80)
                    print("Sorry Wrong username or password!  Try again...")
                    session_name = input("\n Username: ")
                    session_pass = getpass.getpass("\n Password: ")
                else:
                    print("User successfully logged in! \n")
                    break
        print("Use the following short codes to navigate the app \n cc-Create Credential \n fc-Find Credential by account \n dc-Display Credentials \n del-Delete Credential \n ex-Logout") 
        break
        #else:
            #print("Sorry I did not get that!!! Try again, this time using \lg\ or \login\ \n")

if __name__ == '__main__':
    '''
    Executes main function if main function hasn't been imported
    '''
    main()
