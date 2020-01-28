#!/usr/bin/env python3.6

from classes import Credentials
from classes import User
from classes import style
import time, sys, random,string, getpass, re, inquirer, os, progressbar
# re - regular expression(Part of inquirer requirements); inquirer - choice selection;  progressbar- progress bar loading
# random - randomize; getpass - terminal password & user engagement;  

# Functions to implement class methods and function
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
    new_credential = Credentials(account_name,user_name,password)
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
    # Initial loading animation
    animation = "|/-\\"
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write("Please wait while setting up")
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    # Entry Greeting
    print("Hello, Welcome to Password Locker, What is your name?")
    user_name = input()
    
    if user_name:
        print(f"\n Welcome {user_name},let me help you to create an account to use Password Locker \n")
    else:
        print("\n Weeelll, Since I don't know your name, let me call you User!!! Let us create an account then\n")

    print("--" * 80)
    # Sign Up with password confirmation
    login_name = input(style.cyan(">>> Enter the username you would like to use \n"))
    login_password = getpass.getpass(style.cyan(">>> Enter the password you want to use \n"))
    confirm_password = getpass.getpass(style.cyan(">>> Confirm your password \n"))
    while True:
        if login_password != confirm_password:
            print(style.red("Passwords do not match!!"))
            login_password = getpass.getpass(">>> Reenter the password  \n")
            confirm_password = getpass.getpass(">>> Reconfirm your password \n")
        else:
            print(style.green("Account Successfully created \n") + style.reset(""))
            break
    time.sleep(1)
    # Login to user Account
    while True:
        login = input(style.red("Status:") + style.yellow("Logged Out \n")+ style.reset("Login to your account using the short code \lg\ or \login\ \n"))
        if login == 'lg' or login.lower() == 'login':
            session_name = input("\n Username: ")
            session_pass = getpass.getpass("\n Password: ")
            print(style.blue("Authenticating Credentials....") + style.reset(""))
            # Code for loading progress bar
            for i in progressbar.progressbar(range(100)):
                time.sleep(0.02)
            time.sleep(1)
            # Confirm that the correct password is entered
            while True:
                if session_name != login_name or session_pass != login_password:
                    print("--" *80)
                    print("Sorry Wrong username or password!  Try again...")
                    session_name = input("\n Username: ")
                    session_pass = getpass.getpass("\n Password: ")
                    for i in progressbar.progressbar(range(100)):
                        time.sleep(0.02)
                        time.sleep(1)
                else:
                    print(style.green("User successfully logged in! \n")+style.reset(""))
                    break
            break
        else:
            print(style.red("\n Sorry I did not get that!!! Try again, this time using \lg\ or \login\ ") + style.reset(""))
    
    print("--" *80)
    # Ask user what they want to do!
    while True:
        user_input = input("Use the following short codes to navigate the app \n" + style.yellow("cc") + style.cyan("-Create Credential \n") + style.yellow("fc") + style.cyan("-Find Credential by account \n") + style.yellow("dc") + style.cyan("-Display Credentials \n") + style.yellow("del") + style.cyan("-Delete Credential \n") + style.yellow("ex") + style.cyan("-Logout \n") + style.reset(""))
        # Logic to create credentials
        if user_input == 'cc':
            # Using inquirer module to create choice selections
            question_create = [inquirer.List('account',message='Are you adding a new or existing account?',choices=['New','Existing'],),]
            answer_create = inquirer.prompt(question_create)
            user_choice = answer_create.get('account','')
            # Create new or existing credential
            if user_choice == 'Existing':
                account_name = input("What is the account you wish to add? \n")
                user_name = input("What is your username on {} \n".format(account_name))
                credential_password = input("What is the password you use for {} \n".format(user_name))

            else:
                account_name = input("What is the account you wish to add? \n")
                user_name = input("What username do you wish to use on {} \n".format(account_name))
                question_yesno = [inquirer.List('account',message='Do you want to have an autogenerated password', choices=['yes','no'])]
                answer_create = inquirer.prompt(question_yesno)
                answer_yesno = answer_create.get('account', '')
                # Ask whether to auto-generate password
                if answer_yesno == 'no':
                    user_password = input("What is the password you use for {} \n".format(user_name))
                    credential_password = user_password
                else:
                    user_length = input("What is the length of the password you wish to generate? \n")
                    # Error handling if user inputs text
                    while True:
                        try:
                            password_length = int(user_length)
                        except ValueError:
                            print("Sorry that is not a number!! Try again!")
                            password_length = input("What is the length of the password you wish to generate? \n")
                            break
                    # Function to generate random passwords
                    def generate_random(pass_length):
                        '''
                        Function to generate random password
                        '''
                        lettersAndDigits = string.ascii_letters + string.digits
                        return ''.join(random.choice(lettersAndDigits) for i in range(int(pass_length)))
                    credential_password = generate_random(password_length)
                    print("Your auto-generated password of {} characters is {}".format(password_length,credential_password))
            question_save = [inquirer.List('save', message='Would you like to save your credentials?', choices=['yes','no'])]
            question_saved = inquirer.prompt(question_save)
            answer_save = question_saved.get('save', '')
            # User prompted whether or not to save credential
            if answer_save == 'no':
                print(f'Your credential {account_name} has been discarded')
            else:
                save_credential(create_credentials(account_name,user_name,credential_password))
                time.sleep(1.5)
                print(f"Your credential for {account_name}: {user_name} & {credential_password} has been saved")
        # Logic to display credentials if any
        elif user_input == 'dc':
            if display_credentials():
                print('Here are your credentials \n' + '-'*20)
                for credential in display_credentials():
                    print("-"*40)
                    print(f"| Account: {credential.account_name} | UserName: {credential.user_name} | Password: {credential.password} |")
                    print("-"*40 + "\n")

            else:
                print("\n You don't seem to have any saved credentials yet!! \n")
        # Logic to find credentials; First checks if credentials exist then calls find_credential method
        elif user_input == 'fc':
            search_account = input("Enter the account you wish to searh for")
            if credential_exist(search_account):
                found_account = find_credential(search_account)
                print("-"*40)
                print(f"| Account: {found_account.account_name} | UserName: {found_account.user_name} | Password: {found_account.password} |")
                print("-"*40 + "\n")
                copy_question = [inquirer.List('copy',message='Do you wish to copy account\'s password to clipboard?',choices=['yes','no'])]
                copy_answer = inquirer.prompt(copy_question)
                copy_response = copy_answer.get('copy','')
                # Prompt user to save a credential if it is saved
                if copy_response == 'no':
                    continue
                else:
                    copy_password(found_account.account_name)
                    print('Password successfully copied to clipboard')

            else:
                print(f"Sorry it seems the Credential {search_account} does not exist")
        # Logic for user to delete credential
        elif user_input == 'del':
            search_delete = input("Enter the account credentials you wish to delete:")
            if credential_exist(search_delete):
                to_delete = find_credential(search_delete)
                sure_question = [inquirer.List('sure',message='Are you sure you wish to delete the credential?',choices=['yes','no'])]
                sure_answer = inquirer.prompt(sure_question)
                sure_response = sure_answer.get('sure','')
                if sure_response == 'no':
                    print(f"Credential for {to_delete.account_name} will not be deleted")
                else:
                    print(f"Credential for {to_delete.account_name} will be deleted")
                    delete_credential(to_delete)
                    print("Credential deleted")
            else:
                print(f"Account {search_delete} does not exist")
        # Logic for user to logout credential
        elif user_input == 'ex':
            quit_question = [inquirer.List('quit',message='Before you leave, would you want to export saved credentials?',choices=['yes','no'])]
            quit_answer = inquirer.prompt(quit_question)
            quit_response = quit_answer.get('quit','')
            # Prompt user whether to export the credentials to another file.
            if quit_response == 'no':
                print("Bye")
                sys.stdout.write("\r (•◡•)")
                print("\n")
            else:
                with open("exports.txt", "w") as handle:
                    if display_credentials():
                        for credential in display_credentials():
                            handle.write(f"| Account: {credential.account_name} | UserName: {credential.user_name} | Password: {credential.password} |")            
                print("Credentials exported \n Bye")
                sys.stdout.write("\r (•◡•)")
                print("\n")
            break
        else:
            print(style.red("Sorry, I did not get that!") + style.reset(""))




if __name__ == "__main__":
    '''
    Executes main function if main function hasn't been imported
    '''
    main()
