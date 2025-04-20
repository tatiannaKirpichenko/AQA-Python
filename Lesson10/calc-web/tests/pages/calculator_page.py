import logging

from tests.locators.calculator_page_locators import CalculatorPageLocators


class CalculatorPage:
    def __init__(self, driver):
        super(CalculatorPage, self).__init__()
        self.driver = driver


    def set_firstOperand(self, value):
        logging.info(f'Setting first operand to: {value}')
        first_operand = self.driver.find_element(*CalculatorPageLocators.first_operand)
        first_operand.clear()
        first_operand.send_keys(value)

    def set_operation(self, value):
        logging.info(f'Setting second operand to: {value}')
        operation = self.driver.find_element(*CalculatorPageLocators.second_operand)
        operation.clear()
        operation.send_keys(value)

    def set_secondOperand(self, value):
        logging.info('Clicking the calculate button.')
        second_operand = self.driver.find_element(*CalculatorPageLocators.second_operand)
        second_operand.clear()
        second_operand.send_keys(value)

    def click_calc_button(self):
        calc_button = self.driver.find_element(*CalculatorPageLocators.calc_button)
        calc_button.click()

    def get_result(self):
        return self.driver.find_element(*CalculatorPageLocators.result).text

    def get_pageCalculator(self):
        return self.driver.find_element(*CalculatorPageLocators.page_calculator)


