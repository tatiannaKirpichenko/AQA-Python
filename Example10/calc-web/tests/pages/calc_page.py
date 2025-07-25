import logging

from tests.locators.calc_page_locators import CalculatorPageLocators


class CalculatorPage:
    def __init__(self, driver):
        super(CalculatorPage, self).__init__()
        self.driver = driver

    def calc_result(self):
        self.get_result

    def calc_add(self, first_operand, second_operation):
        self.set_firstOperand(first_operand)
        self.set_secondOperand(second_operation)
        self.click_calc_button()

    def calc_subtraction(self, first_operand, second_operation):
        self.set_firstOperand(first_operand)
        self.select_subtraction()
        self.set_secondOperand(second_operation)
        self.click_calc_button()

    def set_firstOperand(self, value):
        first_operand = self.driver.find_element(*CalculatorPageLocators.first_operand)
        first_operand.clear()
        first_operand.send_keys(value)

    def set_operation(self, value):
        operation = self.driver.find_element(*CalculatorPageLocators.operation)
        operation.clear()
        operation.send_keys(value)

    def set_secondOperand(self, value):
        second_operand = self.driver.find_element(*CalculatorPageLocators.second_operand)
        second_operand.clear()
        second_operand.send_keys(value)

    def select_subtraction(self):
        select_element = self.driver.find_element(*CalculatorPageLocators.operation)
        from selenium.webdriver.support.ui import Select
        select = Select(select_element)
        select.select_by_value('-')

    def click_calc_button(self):
        logging.info(f'clicking "Calc" button')
        calc_button = self.driver.find_element(*CalculatorPageLocators.calc_button)
        calc_button.click()


    def get_result(self):
        logging.info(f'calc result')
        result_element = self.driver.find_element(*CalculatorPageLocators.result)
        result_text = result_element.get_attribute('value')
    #   print(f"Значение результата: {result_text}")
        try:
            result_number =  int (result_text)
            return result_number
        except ValueError:
            logging.error(f"Не удалось преобразовать результат '{result_text}' в число.")
            return None

    def get_pageCalculator(self):
        return self.driver.find_element(*CalculatorPageLocators.page_calculator)


