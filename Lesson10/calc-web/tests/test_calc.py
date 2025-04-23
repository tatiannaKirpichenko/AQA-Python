import logging
from datetime import datetime
import os
import allure

from selenium import webdriver
from pages.login_page import LoginPage
from pages.calc_page import CalculatorPage


class TestCalculate:
    page_url = 'http://127.0.0.1:7000/'

    def setup_method(self):
        if not os.path.isdir('./tests/screenshots'):
            os.mkdir('./tests/screenshots')
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.page_url)
        self.login_page = LoginPage(self.driver)
        self.calc_page = CalculatorPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def save_screenshot(self, name):
        path = './tests/screenshots'
        name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + f'__{name}.png'
        logging.debug(f'saving screenshot {name}')
        self.driver.save_screenshot(path + name)
        allure.attach.file(source=path + name, attachment_type=allure.attachment_type.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Login as admin with valid password and check the addition of two positive numbers')
    def test_additionPositiveNumbers_SuccessfulLoginAndValidResult(self):
        logging.info('trying to log in as valid user')
        self.login_page.log_in('admin','123')
        logging.info('trying to add up for positive numbers')
        self.calc_page.calc_add('5','3')
        logging.info('checking the receipt of the calculation result')
        result_number = self.calc_page.get_result()
        assert 8 == result_number
        self.driver.save_screenshot('./tests/screenshots/test_additionPositiveNumbers_SuccessfulLoginAndValidResult.png')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Login as admin with valid password and check the subtraction of two positive numbers')
    def test_subtractionPositiveNumbersResultPositiveNumber_SuccessfulLoginAndValidResult(self):
        logging.info('trying to log in as valid user')
        self.login_page.log_in('admin', '123')
        logging.info('trying to subtract positive numbers.')
        self.calc_page.calc_subtraction('10', '3' )
        logging.info('checking the receipt of the calculation result')
        result_number = self.calc_page.get_result()
        assert 7 == result_number
        self.driver.save_screenshot(f'./tests/screenshots/'
                                    f'test_subtractionPositiveNumbersResultPositiveNumber_SuccessfulLoginAndValidResult.png')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        'Login as admin with valid password and check the subtraction of two positive numbers resulting in a negative number')
    def test_subtractionPositiveNumbersResultNegativeNumber_SuccessfulLoginAndValidResult(self):
        logging.info('trying to log in as valid user')
        self.login_page.log_in('admin', '123')
        logging.info('trying to subtract positive numbers.')
        self.calc_page.calc_subtraction('10', '15')
        logging.info('checking the receipt of the calculation result')
        result_number = self.calc_page.get_result()
        assert -5 == result_number
        self.driver.save_screenshot(f'./tests/screenshots/'
                                    f'test_subtractionPositiveNumbersResultNegativeNumber_SuccessfulLoginAndValidResult.png')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Login as admin with valid password and check the addition of two negative numbers')
    def test_additionNegativeNumbers_SuccessfulLoginAndValidResult(self):
        logging.info('trying to log in as valid user')
        self.login_page.log_in('admin', '123')
        logging.info('trying to add up for negative numbers')
        self.calc_page.calc_add('-5', '-3')
        logging.info('checking the receipt of the calculation result')
        result_number = self.calc_page.get_result()
        assert -8 == result_number
        self.driver.save_screenshot(f'./tests/screenshots/'
                                    f'test_additionNegativeNumbers_SuccessfulLoginAndValidResult.png')




