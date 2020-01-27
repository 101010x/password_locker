import unittest
from classes import Credentials
from classes import User 
import pyperclip

class TestCredential(unittest.TestCase):
    '''
    Test class that defines the test functions for the Credentials class

    Args:
        unittest.case: Testcase class that helps in defining test cases
    '''

    def setUp(self):
        '''
        SetUp method that is performed everytime a test case is run
        '''
        self.new_credentials = Credentials("instagram","usertest","userpass")

    def tearDown(self):
        '''
        TearDown method that cleans up after every test case
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        Test if object is correctly initialized
        '''
        self.assertEqual(self.new_credentials.account_name, "instagram")
        self.assertEqual(self.new_credentials.user_name,"usertest")
        self.assertEqual(self.new_credentials.password, "userpass")
    
    def test_save_credential(self):
        '''
        Test the function to save credentials
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        Test the saving of multiple credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "Bot", "root")
        random_credentials = Credentials("Spotify", "user", "username")
        test_credentials.save_credentials()
        random_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 3)

    def test_delete_credential(self):
        '''
        Test the deletion of one credential
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "Bot", "root")
        random_credentials = Credentials("Spotify", "user", "username")
        test_credentials.save_credentials()
        random_credentials.save_credentials()
        random_credentials.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_find_by_account_name(self):
        '''
        Test finding an account by it's name
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "Bot", "root")
        random_credentials = Credentials("Spotify", "user", "username")
        test_credentials.save_credentials()
        random_credentials.save_credentials()
        
        found_account = Credentials.find_by_account_name("Spotify")
        self.assertEqual(random_credentials.account_name, found_account.account_name)


    def test_credential_exist(self):
        '''
        Test that a credential exists
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter", "Bot", "root")
        random_credentials = Credentials("Spotify", "user", "username")
        test_credentials.save_credentials()
        random_credentials.save_credentials()
        
        account_exists = Credentials.account_exists("Spotify")
        self.assertTrue(account_exists)

    def test_display_credentials(self):
        '''
        Test that credentials can be displayed
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

    def test_copy_password(self):
        '''
        Test to copy the password to the clipboard
        '''
        self.new_credentials.save_credentials()
        Credentials.copy_password("instagram")
        self.assertEqual(self.new_credentials.password, pyperclip.paste())

class TestUser(unittest.TestCase):
    '''
    Test class that defines test case for user class

    Args:
        unittest.TestCase: Class that helps defining test cases
    '''
    def setUp(self):
        '''
        Prepare for each test case
        '''
        self.new_user = User("Mutugi", "helloworld")

    def tearDown(self):
        '''
        Clean up after every test case
        '''
        User.user_list = []

    def test_init(self):
        '''
        Test the initialization of the list correctly
        '''
        self.assertEqual(self.new_user.name,"Mutugi")
        self.assertEqual(self.new_user.password, "helloworld");


if __name__ == '__main__':
    unittest.main()

