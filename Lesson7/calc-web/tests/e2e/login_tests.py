import unittest

from selenium import webdriver

from pages.login_page import LoginPage


class LoginTests(unittest.TestCase):
    page_url = 'http://127.0.0.1:7000/'

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.page_url)

        self.login_page = LoginPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()
        super().tearDown()

    def test_InvalidUser_ErrorMessageShown(self):
        self.login_page.set_username('fake-user')
        self.login_page.set_password('fake-user')
        self.login_page.click_login_button()

        self.assertTrue(self.login_page.is_username_error_message_shown())
        error_message_text = self.login_page.get_username_error_text()
        self.assertEqual('Invalid user name', error_message_text)

    def test_InvalidPassword_ErrorMessageShown(self):
        self.login_page.set_username('admin')
        self.login_page.set_password('fake-user')
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.is_password_error_message_shown())
        error_message_text = self.login_page.get_password_error_text()
        self.assertEqual('Invalid user name', error_message_text)

    def test_InvalidUserAndPassword_ErrorMessagesShown(self):
        self.login_page.set_username('fake-user')
        self.login_page.set_password('wrong-password')
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.is_username_error_message_shown())
        self.assertTrue(self.login_page.is_password_error_message_shown())
        username_error_text = self.login_page.get_username_error_text()
        password_error_text = self.login_page.get_password_error_text()
        self.assertEqual('Invalid user name', username_error_text)
        self.assertEqual('Invalid user name', password_error_text)

    def test_EmptyUsername_ErrorMessageShown(self):
        self.login_page.set_username('')
        self.login_page.set_password('some-password')
        self.login_page.click_login_button()

        self.assertTrue(self.login_page.is_username_error_message_shown())
        error_message_text = self.login_page.get_username_error_text()
        self.assertEqual('Invalid user name', error_message_text)

    def test_EmptyPassword_ErrorMessageShown(self):
        self.login_page.set_username('valid-user')
        self.login_page.set_password('')
        self.login_page.click_login_button()

        self.assertTrue(self.login_page.is_password_error_message_shown())
        error_message_text = self.login_page.get_username_error_text()
        self.assertEqual('Invalid user name', error_message_text)
