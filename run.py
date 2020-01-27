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



if __name__ == '__main__':
    '''
    Executes main function if main function hasn't been imported
    '''
    main()
