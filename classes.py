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
