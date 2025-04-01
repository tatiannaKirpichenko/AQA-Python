import json
import unittest
from app import application
from app.services.AuthService import AuthService
from configuration import TestConfig


class CalculateTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.calculator = None

    def setUp(self) -> None:
        super().setUp()
        application.config.from_object(TestConfig)
        self.client = application.test_client()
        AuthService.tokens = {}

    def test_Calculator_ValidAdditionOperation_LoginSuccessAndTokenReturned(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        self.assertEqual('success', login_response_data['status'])
        self.assertIsNotNone(login_response_data['data']['token'])

        token = login_response_data['data']['token']

        calculation_data = {
            'op1': 5,
            'operation': '+',
            'op2': 3
        }
        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})


        self.assertEqual(200, calculation_response.status_code)
        calculation_response_data = json.loads(calculation_response.get_data())
        self.assertEqual('success', calculation_response_data['status'])
        self.assertEqual(8, calculation_response_data['data'])

    def test_Calculator_ValidSubtractionOperation_LoginSuccessAndTokenReturned(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        self.assertEqual('success', login_response_data['status'])
        self.assertIsNotNone(login_response_data['data']['token'])

        token = login_response_data['data']['token']

        calculation_data = {
            'op1': 10,
            'operation': '-',
            'op2': 3
        }
        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})


        self.assertEqual(200, calculation_response.status_code)
        calculation_response_data = json.loads(calculation_response.get_data())
        self.assertEqual('success', calculation_response_data['status'])
        self.assertEqual(7, calculation_response_data['data'])


    def test_Calculator_ValidResultAdditionTwoNegativeNumbers_LoginSuccessAndTokenReturned(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        self.assertEqual('success', login_response_data['status'])
        self.assertIsNotNone(login_response_data['data']['token'])

        token = login_response_data['data']['token']

        calculation_data = {
            'op1':-5,
            'operation': '-',
            'op2': -8
        }
        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        self.assertEqual(200, calculation_response.status_code)
        calculation_response_data = json.loads(calculation_response.get_data())
        self.assertEqual('success', calculation_response_data['status'])
        self.assertEqual(3, calculation_response_data['data'])

    def test_Calculator_ValidResultSubtractionTwoNegativeNumbers_LoginSuccessAndTokenReturned(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        self.assertEqual('success', login_response_data['status'])
        self.assertIsNotNone(login_response_data['data']['token'])

        token = login_response_data['data']['token']

        calculation_data = {
            'op1':10,
            'operation': '-',
            'op2': -15
        }
        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        self.assertEqual(200, calculation_response.status_code)
        calculation_response_data = json.loads(calculation_response.get_data())
        self.assertEqual('success', calculation_response_data['status'])
        self.assertEqual(25, calculation_response_data['data'])


    def test_Calculator_enterStringInsteadOfNumber_LoginSuccessAndTokenReturned(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        self.assertEqual('success', login_response_data['status'])
        self.assertIsNotNone(login_response_data['data']['token'])

        token = login_response_data['data']['token']

        calculation_data = {
            'op1': 'string1',
            'operation': '+',
            'op2': 'string2'
        }
        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        self.assertEqual(500, calculation_response.status_code)
        calculation_response_data = json.loads(calculation_response.get_data())
        self.assertEqual('error', calculation_response_data['status'])
        self.assertIn('message', calculation_response_data)

    def test_Calculator_enterNothing_LoginSuccessAndTokenReturned(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        self.assertEqual('success', login_response_data['status'])
        self.assertIsNotNone(login_response_data['data']['token'])

        token = login_response_data['data']['token']

        calculation_data = {
            'op1': '',
            'operation': '+',
            'op2': ''
        }
        calculation_response = self.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': token})

        self.assertEqual(500, calculation_response.status_code)
        calculation_response_data = json.loads(calculation_response.get_data())
        self.assertEqual('error', calculation_response_data['status'])
        self.assertIn('message', calculation_response_data)












