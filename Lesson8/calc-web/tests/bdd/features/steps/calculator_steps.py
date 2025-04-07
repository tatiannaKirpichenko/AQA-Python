import json

from behave import given, when, then

from app import application
from configuration import TestConfig

@given('the application is running')
def step_application_running(context):
    context.client = application.test_client()
    application.config.from_object(TestConfig)

@given('valid login credentials')
def step_valid_login_credentials(context):
    context.login_data = {
        'userName': 'admin',
        'password': '123'
    }

@when('login with username "{user_name}" and password "{password}"')
def step_login(context, user_name, password):
    context.login_data['userName'] = user_name
    context.login_data['password'] = password

    login_response = context.client.post('/login', data=json.dumps(context.login_data), content_type='application/json')
    context.login_response_data = json.loads(login_response.get_data())
    context.token = context.login_response_data['data']['token']

@then('the login response status should be "{expected_status}"')
def step_assert_login_status(context, expected_status):
    assert context.login_response_data['status'] == expected_status

@then('a token should be returned')
def step_assert_token(context):
    assert context.token is not None

@when('addition with operands {op1} and {op2}')
def step_perform_addition(context, op1, op2):
    calculation_data = {
        'op1': op1,
        'operation': '+',
        'op2': op2
    }
    calculation_response = context.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': context.token})
    context.calculation_response_data = json.loads(calculation_response.get_data())


@when('subtraction with operands {op1} and {op2}')
def step_perform_subtraction(context, op1, op2):
    calculation_data = {
        'op1': op1,
        'operation': '-',
        'op2': op2
    }
    calculation_response = context.client.post('/calc', data=json.dumps(calculation_data),
                                                content_type='application/json',
                                                headers={'x-auth-token': context.token})
    context.calculation_response_data = json.loads(calculation_response.get_data())

@when('addition with different operands {op1} and {op2}')
def perform_calculation(context,op1,op2):
    calculation_data = {
        'op1': op1,
        'operation': '+',
        'op2': op2
    }
    context.calculation_response = context.client.post('/calc', data=json.dumps(calculation_data),
                                                       content_type='application/json',
                                                       headers={'x-auth-token': context.token})

@when('division with operands {op1} and {op2}')
def step_perform_division(context, op1, op2):
        calculation_data = {
            'op1': op1,
            'operation': '/',
            'op2': op2
        }
        context.calculation_response = context.client.post('/calc', data=json.dumps(calculation_data),
                                                   content_type='application/json',
                                                   headers={'x-auth-token': context.token})


@then('the calculation response status should be "{expected_status}"')
def step_assert_calculation_status(context, expected_status):
    assert context.calculation_response_data['status'] == expected_status

@then('the result should be {expected_result:d}')
def step_assert_result(context, expected_result):
    assert context.calculation_response_data['data'] == expected_result


@then('the response should indicate an error')
def step_impl(context):
    assert context.calculation_response.status_code == 500
    calculation_response_data = json.loads(context.calculation_response.get_data())
    assert calculation_response_data['status'] == 'error'
    assert 'message' in calculation_response_data


@then('the response should indicate a failure with a message')
def check_failure_response(context):
    assert context.calculation_response.status_code == 200
    calculation_response_data = json.loads(context.calculation_response.get_data())
    assert calculation_response_data['status'] == 'fail'
    assert 'message' in calculation_response_data




















