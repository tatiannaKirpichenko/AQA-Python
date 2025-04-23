from selenium.webdriver.common.by import By


class CalculatorPageLocators:

    first_operand=(By.ID,'firstOperand')
    operation=(By.CSS_SELECTOR,'select#operation')
    second_operand=(By.ID,'secondOperand')
    calc_button=(By.ID,'submitCalc')
    result=(By.ID,'result')
    page_calculator=(By.ID,'calcView')
