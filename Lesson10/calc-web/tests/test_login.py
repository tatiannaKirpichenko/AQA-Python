import logging
from datetime import datetime
import os
import allure
from selenium import webdriver

from pages.login_page import LoginPage


class TestLogin:
    page_url = 'http://127.0.0.1:7000/'

    def setup_method(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.page_url)
        self.login_page = LoginPage(self.driver)

        self.screenshot_dir = 'screenshots'
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
            logging.info('Screenshot directory created at: %s', self.screenshot_dir)

    def teardown_method(self):
        self.driver.close()

    def save_screenshot(self, name):
        path = './tests/screenshots'
        name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + f'__{name}.png'
        logging.debug(f'saving screenshot {name}')
        self.driver.save_screenshot(path + name)
        allure.attach.file(source=path + name, attachment_type=allure.attachment_type.PNG)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Login with invalid credentials and check that username error message is shown')
    def test_InvalidUser_ErrorMessageShown(self):
        logging.info('Trying to log in with invalid username and password')
        self.login_page.log_in('fake-user', 'fake-user')
        self.login_page.click_login_button()

        logging.info('Checking if username error message is shown')
        assert True == self.login_page.is_username_error_message_shown()
        error_message_text = self.login_page.get_username_error_text()
        assert 'Invalid user name' == error_message_text
        self.driver.save_screenshot(f'./tests/screenshots/test_InvalidUser_ErrorMessageShown.png')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Login with valid username and invalid password and check that password error message is shown')
    def test_InvalidPassword_ErrorMessageShown(self):
        logging.info('Trying to log in with valid username and invalid password')
        self.login_page.log_in('admin', 'fake-user')
        self.login_page.click_login_button()

        logging.info('Checking if password error message is shown')
        assert True == self.login_page.is_password_error_message_shown()
        error_message_text = self.login_page.get_password_error_text()
        assert 'Invalid user name' == error_message_text
        self.driver.save_screenshot(f'./tests/screenshots/test_InvalidPassword_ErrorMessageShown.png')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Login with empty username and valid password and check that username error message is shown')
    def test_EmptyUsername_ErrorMessageShown(self):
        logging.info('Trying to log in with empty username and valid password')
        self.login_page.log_in(' ', 'some-password')
        self.login_page.click_login_button()

        logging.info('Checking if username error message is shown')
        assert True == self.login_page.is_username_error_message_shown()
        error_message_text = self.login_page.get_username_error_text()
        assert 'Invalid user name' == error_message_text
        self.driver.save_screenshot(f'./tests/screenshots/test_EmptyUsername_ErrorMessageShown.png')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Login with valid username and empty password and check that password error message is shown')
    def test_EmptyPassword_ErrorMessageShown(self):
        logging.info('Checking if user name error message is shown')
        self.login_page.log_in('valid-user', ' ')
        self.login_page.click_login_button()

        logging.info('Checking if password error message is shown')
        assert True == self.login_page.is_password_error_message_shown()
        error_message_text = self.login_page.get_username_error_text()
        logging.info(f'Error message text: {error_message_text}')
        assert 'Invalid user name' == error_message_text
        self.driver.save_screenshot(f'./tests/screenshots/test_EmptyPassword_ErrorMessageShown.png')
