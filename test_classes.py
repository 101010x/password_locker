import unittest
from classes import Credentials
import pyperclip

class TestCredential(unittest.TestCase):
    '''
    Test class that defines the test functions for the Credentials class

    Args:
        unittest.case: Testcase class that helps in defining test cases
    '''

    def setUp(self):
        '''
        SetUp method that id s performed everytime a test case is run
        '''
        self.new_credentials = Credentials("instagram","usertest","userpass")

    def tearDown(self):
        '''
        TearDown method that cleans up after every test case
        '''
        Credentials.credentials = []

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
        self.new_credentials.save_credential()
        self.assertEqual(len(self.new_credentials),1)

if __name__ == '__main__':
    unittest.main()

