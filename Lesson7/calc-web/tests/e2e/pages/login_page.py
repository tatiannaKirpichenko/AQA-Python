from tests.e2e.locators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        super(LoginPage, self).__init__()
        self.driver = driver

    def set_username(self, value):
        username = self.driver.find_element(*LoginPageLocators.username_input)
        username.clear()
        username.send_keys(value)

    def set_password(self, value):
        password = self.driver.find_element(*LoginPageLocators.password_input)
        password.clear()
        password.send_keys(value)

    def click_login_button(self):
        login_button = self.driver.find_element(*LoginPageLocators.login_button)
        login_button.click()

    def is_username_error_message_shown(self):
        user_name_error_message = self.driver.find_element(*LoginPageLocators.username_error_message)
        return user_name_error_message.value_of_css_property('display') == 'block'

    def get_username_error_text(self):
        return self.driver.find_element(*LoginPageLocators.username_error_message).text

    def is_password_error_message_shown(self):
        password_error_message = self.driver.find_element(*LoginPageLocators.username_error_message)
        return password_error_message.value_of_css_property('display') == 'block'

    def get_password_error_text(self):
        return self.driver.find_element(*LoginPageLocators.username_error_message).text


