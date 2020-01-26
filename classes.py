import pyperclip

class Credentials:
    '''
    Class to generate new instances of Credentials
    '''
    credentials = []  # Empty credential list

    def __init__(self, account_name, user_name, password):
        '''
        init method defines properties
        '''

        self.account_name = account_name
        self.user_name = user_name
        self.password = password
