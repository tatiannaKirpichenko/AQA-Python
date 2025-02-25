import unittest

from Lesson2.tasks.src.email_generator import generate_email


class GenerateEmailTestCase(unittest.TestCase):

    def test_GenerateEmail_ValidLocalAndDomainParts_EmailGeneratedWithoutReplacement(self):
        email = 'Petr@rambler.ru'

        generate_result = generate_email('Petr', 'rambler.ru')

        self.assertEqual(email, generate_result)

    def test_GenerateEmail_ValidLocalPartsContainingDotAndDomainParts_EmailGeneratedWithoutReplacement(self):
        email = 'Petr.Ivanov@gmail.com'

        generate_result = generate_email('Petr.Ivanov', 'gmail.com')

        self.assertEqual(email, generate_result)

    def test_GenerateEmail_ExclamationMarkInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(self):
        email = 'Petr.Ivanov__@gmail.com'

        generate_result = generate_email('Petr.Ivanov!!', 'gmail.com')

        self.assertEqual(email, generate_result)

    def test_GenerateEmail_PercentSignInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(self):
        email = 'Petr_Ivan_ov@gmail.com'

        generate_result = generate_email('Petr%Ivan%ov', 'gmail.com')

        self.assertEqual(email, generate_result)

    def test_GenerateEmail_DollarSignInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(self):
        email = 'Petr__Ivan__ov@gmail.com'

        generate_result = generate_email('Petr$$Ivan$$ov', 'gmail.com')

        self.assertEqual(email, generate_result)

    def test_GenerateEmail_ExclamationAndPercentAndDollarSignInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(
            self):
        email = 'Petr_Ivan_ov_@gmail.com'

        generate_result = generate_email('Petr!Ivan%ov$', 'gmail.com')

        self.assertEqual(email, generate_result)

    def test_GenerateEmail_questionMarkInLocalPart_EmailDoesNotReplaceWithExpectedCharacter(self):
        email = 'Petr_@rambler.ru'

        generate_result = generate_email('Petr?', 'rambler.ru')

        self.assertNotEqual(email, generate_result)

    def test_GenerateEmail_NoUsernameInEmail_EmailNotCreated(self):
        email = '@gmail.com'

        generate_result = generate_email(' ', 'gmail.com')

        self.assertNotEqual(email, generate_result)

    def test_GenerateEmail_NotValidEmptyDomainPart_EmailNotCreated(self):
        email = 'PetrPetrov'

        generate_result = generate_email('PetrPetrov', ' ')

        self.assertNotEqual(email, generate_result)
