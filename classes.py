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
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account:
                return credential

    @classmethod
    def account_exists(cls, account):
        '''
        Method to ascertain that an account exists
        '''

        for credential in cls.credentials_list:
            if credential.account_name == account:
                return True

        return False
