import json
import logging
from datetime import datetime
import os
import allure
from app import application
from app.services.AuthService import AuthService
from configuration import TestConfig
from selenium import webdriver



class TestCalculate:

    def setup_method(self):
        application.config.from_object(TestConfig)
        self.client = application.test_client()
        AuthService.tokens = {}

        self.screenshot_dir = 'screenshots'
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
            logging.info('Screenshot directory created at: %s', self.screenshot_dir)

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)


    def teardown_method(self):
        self.driver.quit()

    def save_screenshot(self, name):
        path = './tests/screenshots'
        name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + f'__{name}.png'
        logging.debug(f'saving screenshot {name}')
        self.driver.save_screenshot(path + name)
        allure.attach.file(source=path + name, attachment_type=allure.attachment_type.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Test valid addition operation after successful login and ensure token is returned')
    def test_Calculator_ValidAdditionOperation_LoginSuccessAndTokenReturned(self):
        logging.info('Starting test for valid addition operation with login.')

        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        logging.info('Login response status code: %d', login_response.status_code)
        assert 200 == login_response.status_code

        login_response_data = json.loads(login_response.get_data())
        logging.info('Login response data: %s', login_response_data)
        assert 'success' == login_response_data['status']
        token = login_response_data['data']['token']

        calculation_data = {
            'op1': 5,
            'operation': '+',
            'op2': 3
        }

        logging.info('Sending calculation request: %s', calculation_data)

        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        logging.info('Calculation response status code: %d', calculation_response.status_code)
        assert 200 == calculation_response.status_code

        calculation_response_data = json.loads(calculation_response.get_data())
        logging.info('Calculation response data: %s', calculation_response_data)
        assert 'success' == calculation_response_data['status']
        assert 8 == calculation_response_data['data']

        self.driver.save_screenshot(f'./tests/screenshots/'
                                    f'test_Calculator_ValidAdditionOperation_LoginSuccessAndTokenReturned.png')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Test valid subtraction operation after successful login and ensure token is returned')
    def test_Calculator_ValidSubtractionOperation_LoginSuccessAndTokenReturned(self):
        logging.info('Starting test for valid subtraction operation with login.')

        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        logging.info('Login response status code: %d', login_response.status_code)
        assert 200 == login_response.status_code

        login_response_data = json.loads(login_response.get_data())
        logging.info('Login response data: %s', login_response_data)
        assert 'success' == login_response_data['status']
        assert 'data' in login_response_data and 'token' in login_response_data['data']
        token = login_response_data['data']['token']

        calculation_data = {
            'op1': 10,
            'operation': '-',
            'op2': 3
        }

        logging.info('Sending calculation request: %s', calculation_data)

        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        logging.info('Calculation response status code: %d', calculation_response.status_code)
        assert 200 == calculation_response.status_code

        calculation_response_data = json.loads(calculation_response.get_data())
        logging.info('Calculation response data: %s', calculation_response_data)
        assert 'success' == calculation_response_data['status']
        assert 7 == calculation_response_data['data']

        self.driver.save_screenshot(f'./tests/screenshots/'
                                    f'test_Calculator_ValidSubtractionOperation_LoginSuccessAndTokenReturned.png')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        'Test valid addition operation with two negative numbers after successful login and ensure token is returned')
    def test_Calculator_ValidResultAdditionTwoNegativeNumbers_LoginSuccessAndTokenReturned(self):
        logging.info('Starting test for valid subtraction operation with login.')

        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        logging.info('Login response status code: %d', login_response.status_code)
        assert 200 == login_response.status_code

        login_response_data = json.loads(login_response.get_data())
        logging.info('Login response data: %s', login_response_data)
        assert 'success' == login_response_data['status']
        assert 'data' in login_response_data and 'token' in login_response_data['data']

        token = login_response_data['data']['token']

        calculation_data = {
            'op1': -5,
            'operation': '-',
            'op2': -8
        }

        logging.info('Sending calculation request: %s', calculation_data)

        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        logging.info('Calculation response status code: %d', calculation_response.status_code)
        assert 200 == calculation_response.status_code

        calculation_response_data = json.loads(calculation_response.get_data())
        logging.info('Calculation response data: %s', calculation_response_data)
        assert 'success' == calculation_response_data['status']
        assert 3 == calculation_response_data['data']

        self.driver.save_screenshot(f'./tests/screenshots/'
                                    f'test_Calculator_ValidResultAdditionTwoNegativeNumbers_LoginSuccessAndTokenReturned.png')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        'Test valid subtraction operation with two negative numbers after successful login and ensure token is returned')
    def test_Calculator_ValidResultSubtractionTwoNegativeNumbers_LoginSuccessAndTokenReturned(self):
        logging.info('Starting test for valid subtraction operation with login.')

        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        logging.info('Login response status code: %d', login_response.status_code)
        assert 200 == login_response.status_code

        login_response_data = json.loads(login_response.get_data())
        logging.info('Login response data: %s', login_response_data)
        assert 'success' == login_response_data['status']
        assert 'data' in login_response_data and 'token' in login_response_data['data']

        token = login_response_data['data']['token']

        calculation_data = {
            'op1': 10,
            'operation': '-',
            'op2': -15
        }

        logging.info('Sending calculation request: %s', calculation_data)

        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        logging.info('Calculation response status code: %d', calculation_response.status_code)
        assert 200 == calculation_response.status_code

        calculation_response_data = json.loads(calculation_response.get_data())
        logging.info('Calculation response data: %s', calculation_response_data)
        assert 'success' == calculation_response_data['status']
        assert 25 == calculation_response_data['data']
        self.driver.save_screenshot(f'./tests/screenshots/'
                                    f'test_Calculator_ValidResultSubtractionTwoNegativeNumbers_LoginSuccessAndTokenReturned.png')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        'Test handling of string inputs instead of numbers after successful login and ensure token is returned')
    def test_Calculator_enterStringInsteadOfNumber_LoginSuccessAndTokenReturned(self):
        logging.info('Starting test for valid subtraction operation with login.')

        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        logging.info('Login response status code: %d', login_response.status_code)
        assert 200 == login_response.status_code

        login_response_data = json.loads(login_response.get_data())
        logging.info('Login response data: %s', login_response_data)
        assert 'success' == login_response_data['status']
        assert 'data' in login_response_data and 'token' in login_response_data['data']

        token = login_response_data['data']['token']

        calculation_data = {
            'op1': 'string1',
            'operation': '+',
            'op2': 'string2'
        }

        logging.info('Sending calculation request with invalid data: %s', calculation_data)

        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        logging.info('Calculation response status code: %d', calculation_response.status_code)
        assert 500 == calculation_response.status_code

        calculation_response_data = json.loads(calculation_response.get_data())
        logging.info('Calculation response data: %s', calculation_response_data)
        assert 'error' == calculation_response_data['status']
        assert 'message' in calculation_response_data

        self.driver.save_screenshot(f'./tests/screenshots/'
                                    f'test_Calculator_enterStringInsteadOfNumber_LoginSuccessAndTokenReturned.png')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Test handling of empty inputs after successful login and ensure token is returned')
    def test_Calculator_EnterNothing_LoginSuccessAndTokenReturned(self):
        logging.info('Starting test: Login and calculation with empty inputs')

        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        logging.info('Login response status code: %d', login_response.status_code)
        assert login_response.status_code == 200, "Login failed"

        login_response_data = json.loads(login_response.get_data())
        logging.info('Login response data: %s', login_response_data)
        assert login_response_data['status'] == 'success', "Login was not successful"
        assert 'token' in login_response_data['data'], "Token not found in response"

        token = login_response_data['data']['token']

        calculation_data = {
            'op1': '',
            'operation': '+',
            'op2': ''
        }

        logging.info('Sending calculation request with empty inputs: %s', calculation_data)

        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        logging.info('Calculation response status code: %d', calculation_response.status_code)
        assert calculation_response.status_code == 500, "Expected server error for empty input"

        calculation_response_data = json.loads(calculation_response.get_data())
        logging.info('Calculation response data: %s', calculation_response_data)
        assert calculation_response_data['status'] == 'error', "Expected error status"
        assert 'message' in calculation_response_data, "Error message not found in response"
        self.driver.save_screenshot(f'./tests/screenshots/'
                                    f'test_Calculator_enterNothing_LoginSuccessAndTokenReturned.png')
