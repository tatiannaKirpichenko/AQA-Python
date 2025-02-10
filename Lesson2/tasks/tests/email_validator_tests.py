import unittest

from src.email_validator import validate_email


class EmailValidatorTestCase(unittest.TestCase):
    def test_ValidateEmail_Valid_True(self):
        email = 'blablabla@super.com'

        validation_result = validate_email(email)

        self.assertTrue(validation_result)

