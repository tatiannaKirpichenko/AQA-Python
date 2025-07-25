import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from tests.e2e.pages.calculator_page import CalculatorPage


class CalculatorTests(unittest.TestCase):
    page_url = 'http://127.0.0.1:7000/'

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.page_url)

        self.login_page = LoginPage(self.driver)
        self.calculator_page = CalculatorPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()
        super().tearDown()

    def test_additionPositiveNumbers_SuccessfulLoginAndValidResult(self):
        self.login_page.set_username('admin')
        self.login_page.set_password('123')
        self.login_page.click_login_button()
        self.assertTrue(self.calculator_page.get_pageCalculator())
        self.calculator_page.set_firstOperand('5')
        self.calculator_page.set_operation('+')
        self.calculator_page.set_secondOperand('3')
        self.calculator_page.click_calc_button()
        self.assertTrue('8', self.calculator_page.get_result())


    def test_subtractionPositiveNumbersResultPositiveNumber_SuccessfulLoginAndValidResult(self):
        self.login_page.set_username('admin')
        self.login_page.set_password('123')
        self.login_page.click_login_button()
        self.assertTrue(self.calculator_page.get_pageCalculator())
        self.calculator_page.set_firstOperand('10')
        self.calculator_page.set_operation('-')
        self.calculator_page.set_secondOperand('3')
        self.calculator_page.click_calc_button()
        self.assertTrue('7', self.calculator_page.get_result())

    def test_subtractionPositiveNumbersResultNegativeNumber_SuccessfulLoginAndValidResult(self):
        self.login_page.set_username('admin')
        self.login_page.set_password('123')
        self.login_page.click_login_button()
        self.assertTrue(self.calculator_page.get_pageCalculator())
        self.calculator_page.set_firstOperand('10')
        self.calculator_page.set_operation('-')
        self.calculator_page.set_secondOperand('15')
        self.calculator_page.click_calc_button()
        self.assertTrue('-5', self.calculator_page.get_result())

    def test_additionNegativeNumbers_SuccessfulLoginAndValidResult(self):
        self.login_page.set_username('admin')
        self.login_page.set_password('123')
        self.login_page.click_login_button()
        self.assertTrue(self.calculator_page.get_pageCalculator())
        self.calculator_page.set_firstOperand('-5')
        self.calculator_page.set_operation('+')
        self.calculator_page.set_secondOperand('-3')
        self.calculator_page.click_calc_button()
        self.assertTrue('-8', self.calculator_page.get_result())

    def test_additionPositiveFractionalNumbers_SuccessfulLoginAndValidResult(self):
        self.login_page.set_username('admin')
        self.login_page.set_password('123')
        self.login_page.click_login_button()
        self.assertTrue(self.calculator_page.get_pageCalculator())
        self.calculator_page.set_firstOperand('0.5')
        self.calculator_page.set_operation('+')
        self.calculator_page.set_secondOperand('0.3')
        self.calculator_page.click_calc_button()
        self.assertTrue('0.8', self.calculator_page.get_result())


