import unittest

from src.email_generator import generate_email

class GenerateEmailTestCase(unittest.TestCase):

    def test_valid_email_True(self):

        self.assertEqual(generate_email('Petr','rambler.ru'), 'Petr@rambler.ru')
        self.assertEqual(generate_email('Petr.Ivanov','gmail.com'),'Petr.Ivanov@gmail.com')

    def test_invalid_character_True(self):

        self.assertEqual(generate_email('Petr.Ivanov!!','gmail.com'),'Petr.Ivanov__@gmail.com')
        self.assertEqual(generate_email('Petr$Ivan*ov%','gmail.com'),'Petr_Ivan_ov_@gmail.com')

    def test_invalid_character_False(self):

        self.assertNotEqual(generate_email('Petr~Ivanov?','gmail.com'),'Petr_Ivanov_@gmail.com')