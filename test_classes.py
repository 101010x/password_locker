import unittest
from classes import Credentials
from classes import User
import pyperclip

class TestCredential(unittest.testcase):
    '''
    Test class that defines the test functions for the Credentials class
    '''

    def setUp(self):
        '''
        SetUp method that id s performed everytime a test case is run
        '''
        self.new_credentials = new Credentials("instagram","usertest","userpass")

    def tearDown(self):
        '''
        TearDown method that cleans up after every test case
        '''
        Credentials.credentials = []

