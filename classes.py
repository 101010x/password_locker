import pyperclip

class Credentials:
    '''
    Class to generate new instances of Credentials
    '''
    credentials_list = []  # Empty credential list

    def __init__(self, account_name, user_name, password):
        '''
        init method defines properties
        '''

        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_credentials(self):
        '''
        Function to save credentials to credentials list
        '''

        Credentials.credentials_list.append(self)

    def delete_credential(self):
        '''
        deletes a saved credential from the credential list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account_name(cls,account):
        '''
        Method to find an account present by the account name

        Args:
            account: The name of the account to be queried
        Returns:
            Returns the Credentials that is found
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account:
                return credential

    @classmethod
    def account_exists(cls, account):
        '''
        Method to ascertain that an account exists

        Args:
            account: The name of the account to check if exists
        Returns:
            Returns True if account exists and false if not
        '''

        for credential in cls.credentials_list:
            if credential.account_name == account:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        Method to display the credentials that are present
        '''
        return cls.credentials_list

    @classmethod
    def copy_password(cls, account):
        '''
        Method to copy target account to clipboard
        '''
        credential_found = Credentials.find_by_account_name(account)
        pyperclip.copy(credential_found.password)


class User:
    '''
    Class to generate new instances of User
    '''
    
    user_list = []

    def __init__(self, name, password):
        '''
        Method to initialize the class variables
        '''
        self.name = name
        self.password = password
