import json
import os
from app import application
from app.services.AuthService import AuthService
from configuration import TestConfig
import logging
from datetime import datetime

import allure


class TestCalculate:

    def setup_method(self):
        if not os.path.isdir('./tests/screenshots'):
            os.mkdir('./tests/screenshots')
        application.config.from_object(TestConfig)
        self.client = application.test_client()
        AuthService.tokens = {}

    def save_screenshot(self, name):
        path = './tests/screenshots/'
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

        logging.info(f'Attempting to log in with credentials: {login_data}')
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        assert 200 == login_response.status_code
        logging.info(f'Login response status code: {login_response.status_code}')
        login_response_data = json.loads(login_response.get_data())
        assert 'success' == login_response_data['status']
        logging.info(f'Login response data: {login_response_data}')
        assert login_response_data['data']['token'] is not None, "Token is missing in the response data."
        token = login_response_data['data']['token']
        logging.info(f'Token received: {token}')
        logging.info('Starting test for valid addition operation.')

        calculation_data = {
            'op1': 5,
            'operation': '+',
            'op2': 3
        }

        logging.info(f'Sending calculation request: {calculation_data}')
        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        logging.info(f'Received response with status code: {calculation_response.status_code}')
        assert 200 == calculation_response.status_code
        calculation_response_data = json.loads(calculation_response.get_data())
        logging.info(f'Calculation response data: {calculation_response_data}')
        assert 'success' == calculation_response_data['status']
        expected_result = 8
        actual_result = calculation_response_data['data']
        assert expected_result == actual_result
        if actual_result == expected_result:
            logging.info('The result of the addition operation is correct.')
        else:
            logging.error(f'Expected result was {expected_result} but got {actual_result}.')
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

        logging.info(f'Attempting to log in with credentials: {login_data}')
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        logging.info(f'Login response status code: {login_response.status_code}')
        assert 200 == login_response.status_code
        login_response_data = json.loads(login_response.get_data())
        logging.info(f'Login response data: {login_response_data}')
        assert 'success' == login_response_data['status']
        logging.info(f'Login response data: {login_response_data}')
        token = login_response_data['data']['token']
        logging.info(f'Received token: {token}')

        calculation_data = {
            'op1': 10,
            'operation': '-',
            'op2': 3
        }

        logging.info(f'Sending calculation request: {calculation_data}')
        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        logging.info(f'Received response with status code: {calculation_response.status_code}')
        assert 200 == calculation_response.status_code
        calculation_response_data = json.loads(calculation_response.get_data())
        logging.info(f'Calculation response data: {calculation_response_data}')
        assert 'success' == calculation_response_data['status']
        expected_result = 7
        actual_result = calculation_response_data['data']
        assert expected_result == actual_result
        if actual_result == expected_result:
            logging.info('The result of the addition operation is correct.')
        else:
            logging.error(f'Expected result was {expected_result} but got {actual_result}.')
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

        logging.info(f'Attempting to log in with credentials: {login_data}')
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        logging.info(f'Login response status code: {login_response.status_code}')
        assert 200 == login_response.status_code
        login_response_data = json.loads(login_response.get_data())
        logging.info(f'Login response data: {login_response_data}')
        assert 'success' == login_response_data['status']
        logging.info(f'Login response data: {login_response_data}')
        token = login_response_data['data']['token']
        logging.info(f'Received token: {token}')

        calculation_data = {
            'op1': -5,
            'operation': '-',
            'op2': -8
        }

        logging.info(f'Sending calculation request: {calculation_data}')
        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        logging.info(f'Received response with status code: {calculation_response.status_code}')
        assert 200 == calculation_response.status_code
        calculation_response_data = json.loads(calculation_response.get_data())
        logging.info(f'Calculation response data: {calculation_response_data}')
        assert 'success' == calculation_response_data['status']
        expected_result = 3
        actual_result = calculation_response_data['data']
        assert expected_result == actual_result
        if actual_result == expected_result:
            logging.info('The result of the addition operation is correct.')
        else:
            logging.error(f'Expected result was {expected_result} but got {actual_result}.')
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

        logging.info(f'Attempting to log in with credentials: {login_data}')
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        logging.info(f'Login response status code: {login_response.status_code}')
        assert 200 == login_response.status_code
        login_response_data = json.loads(login_response.get_data())
        logging.info(f'Login response data: {login_response_data}')
        assert 'success' == login_response_data['status']
        logging.info(f'Login response data: {login_response_data}')
        token = login_response_data['data']['token']
        logging.info(f'Received token: {token}')

        calculation_data = {
            'op1': 10,
            'operation': '-',
            'op2': -15
        }

        logging.info(f'Sending calculation request: {calculation_data}')
        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        logging.info(f'Received response with status code: {calculation_response.status_code}')
        assert 200 == calculation_response.status_code
        calculation_response_data = json.loads(calculation_response.get_data())
        logging.info(f'Calculation response data: {calculation_response_data}')
        assert 'success' == calculation_response_data['status']
        expected_result = 25
        actual_result = calculation_response_data['data']
        assert expected_result == actual_result
        if actual_result == expected_result:
            logging.info('The result of the addition operation is correct.')
        else:
            logging.error(f'Expected result was {expected_result} but got {actual_result}.')
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

        logging.info(f'Attempting to log in with credentials: {login_data}')
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        logging.info(f'Login response status code: {login_response.status_code}')
        assert 200 == login_response.status_code
        login_response_data = json.loads(login_response.get_data())
        logging.info(f'Login response data: {login_response_data}')
        assert 'success' == login_response_data['status']
        logging.info(f'Login response data: {login_response_data}')
        token = login_response_data['data']['token']
        logging.info(f'Received token: {token}')

        def perform_calculation(token):
            calculation_data = {
                'op1': 'string1',
                'operation': '+',
                'op2': 'string2'
            }

            logging.info("Sending calculation request with data: %s", calculation_data)
            calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                    content_type='application/json',
                                                    headers={'x-auth-token': token})

            logging.info("Calculation response status code: %d", calculation_response.status_code)
            if calculation_response.status_code == 500:
                calculation_response_data = json.loads(calculation_response.get_data())
                logging.info("Calculation response data: %s", calculation_response_data)

                if calculation_response_data['status'] == 'error' and 'message' in calculation_response_data:
                    logging.info("Error message received as expected: %s", calculation_response_data['message'])
                else:
                    logging.error("Unexpected response format for error case.")
            else:
                logging.error(f"Expected status code 500 but got: {calculation_response.status_code}")
            self.driver.save_screenshot(f'./tests/screenshots/'
                                        f'test_Calculator_enterStringInsteadOfNumber_LoginSuccessAndTokenReturned.png')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Test handling of empty inputs after successful login and ensure token is returned')
    def test_Calculator_enterNothing_LoginSuccessAndTokenReturned(self):

        logging.info('Starting test for valid subtraction operation with login.')

        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        logging.info(f'Attempting to log in with credentials: {login_data}')
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        logging.info(f'Login response status code: {login_response.status_code}')
        assert 200 == login_response.status_code
        login_response_data = json.loads(login_response.get_data())
        logging.info(f'Login response data: {login_response_data}')
        assert 'success' == login_response_data['status']
        logging.info(f'Login response data: {login_response_data}')
        token = login_response_data['data']['token']
        logging.info(f'Received token: {token}')

        def perform_calculation(token):
            calculation_data = {
                'op1': ' ',
                'operation': '+',
                'op2': ' '
            }

            logging.info("Sending calculation request with data: %s", calculation_data)
            calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                    content_type='application/json',
                                                    headers={'x-auth-token': token})

            logging.info("Calculation response status code: %d", calculation_response.status_code)
            if calculation_response.status_code == 500:
                calculation_response_data = json.loads(calculation_response.get_data())
                logging.info("Calculation response data: %s", calculation_response_data)

                if calculation_response_data['status'] == 'error' and 'message' in calculation_response_data:
                    logging.info("Error message received as expected: %s", calculation_response_data['message'])
                else:
                    logging.error("Unexpected response format for error case.")
            else:
                logging.error(f"Expected status code 500 but got: {calculation_response.status_code}")
            self.driver.save_screenshot(f'./tests/screenshots/'
                                        f'test_Calculator_enterNothing_LoginSuccessAndTokenReturned.png')

