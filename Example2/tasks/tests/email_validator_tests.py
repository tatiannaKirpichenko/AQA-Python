import unittest

from Lesson2.tasks.src.email_validator import validate_email


class EmailValidatorTestCase(unittest.TestCase):

    def test_ValidateEmail_Valid_True(self):
        email = 'blablabla@super.com'

        validation_result = validate_email(email)

        self.assertTrue(validation_result)

    def test_ValidateEmail_ValidResultEmail_True(self):
        email = "petr@gmail.com"

        validation_result = validate_email(email)

        self.assertTrue(validation_result)

    def test_ValidateEmail_EmailContainsTwoCommercialCharactersAt_False(self):
        email = 'petr@ivanov@gmail.com'

        validation_result = validate_email(email)

        self.assertFalse(validation_result)
