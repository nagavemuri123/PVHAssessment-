import time
import unittest
from unittest.suite import TestSuite
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import Credentials
from HomePage import HomePage
from MyAccountPage import MyAccountPage
import HtmlTestRunner

import os
script_dir = os.path.dirname(__file__)
driver = os.path.join(script_dir, "drivers\chromedriver.exe")
URL = "https://nl.tommy.com/"

##################################################Test1########################################################
class TestOne(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    def test_that_user_can_create_an_account_with_valid_data(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(5)
        register = HomePage(driver)
        register.accept_agreement()
        register.select_signup()
        time.sleep(5)
        register.enter_email_to_register(email=Credentials.random_char(7)+"@gmail.com")
        register.enter_password_to_register(password=Credentials.password)
        register.verify_password_entered(password=Credentials.password)
        register.accept_condition()
        register.register()
        time.sleep(10)
        MyAccount = MyAccountPage(driver)
        text = MyAccount.get_my_account_text()
        if text == 'MIJN ACCOUNT':

            print("User registered successfully")

        time.sleep(10)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test-1 completed')

#####################################TEST-2##################################################


class TestTwo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    def test_that_registered_user_can_add_a_new_address(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(5)
        register = HomePage(driver)
        register.accept_agreement()
        register.select_signup()
        time.sleep(5)
        email = Credentials.random_char(7)+"@gmail.com"
        password = Credentials.password
        register.enter_email_to_register(email)
        register.enter_password_to_register(password)
        register.verify_password_entered(password)
        register.accept_condition()
        register.register()
        MyAccount = MyAccountPage(driver)
        time.sleep(15)
        MyAccount.go_to_address_book()
        time.sleep(10)
        MyAccount.add_new_address()
        time.sleep(10)
        MyAccount.enter_first_name(fname=Credentials.fName)
        MyAccount.enter_last_name(lname=Credentials.lName)
        MyAccount.enter_street(street=Credentials.street)
        MyAccount.enter_house_number(house_number=Credentials.houseno)
        MyAccount.enter_city(city=Credentials.city)
        MyAccount.enter_zip_code(zip=Credentials.zip)
        MyAccount.save_address()
        time.sleep(10)
        #After hitting save, the My Account page loaded with given address details, in this page title = My Account and sub title is addressbook
        title = MyAccount.get_my_account_text()
        sub_title = MyAccount.get_address_as_subtitle()

        if title == 'MIJN ACCOUNT' and sub_title == 'ADRESBOEK':
            print('address added successfully by newly registered user')

        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test-2 completed')

###############################################TEST-3##########################################
class TestThree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_user_see_specific_error_when_specific_data_not_provided_when_registering(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(5)
        register = HomePage(driver)
        register.accept_agreement()
        register.select_signup()
        time.sleep(5)
        register.enter_empty_email_and_tab()
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).perform()
        register.tab_to_verify_password()
        action.send_keys(Keys.TAB).perform()
        #get invalid messages for empty data in email, password, verify password fields
        message1 = register.invalid_message_for_email()
        message2 = register.invalid_message_for_password()
        message3 = register.invalid_verify_password_message()

        if message1 == message2 == message3 == 'Vul het veld in':
            print('Message displayed correctly for invalid data')
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test-3 completed')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))
    #create a suite()
    suite = TestSuite()
    # Load all tests
    tests = unittest.TestLoader()
    suite1 = suite.addTest(tests.loadTestsFromTestCase(TestOne))
    suite2 = suite.addTest(tests.loadTestsFromTestCase(TestTwo))
    suite3 = suite.addTest(tests.loadTestsFromTestCase(TestThree))

    # Create runner to run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)
