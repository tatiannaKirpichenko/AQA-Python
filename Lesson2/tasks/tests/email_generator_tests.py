import unittest

from Lesson2.tasks.src.email_generator import generate_email


class GenerateEmailTestCase(unittest.TestCase):

    def test_GenerateEmail_ValidLocalAndDomainParts_EmailGeneratedWithoutReplacement(self):
        self.assertEqual(generate_email('Petr', 'rambler.ru'), 'Petr@rambler.ru')

    def test_GenerateEmail_ValidLocalPartsContainingDotAndDomainParts_EmailGeneratedWithoutReplacement(self):
        self.assertEqual(generate_email('Petr.Ivanov', 'gmail.com'), 'Petr.Ivanov@gmail.com')

    def test_GenerateEmail_ExclamationMarkInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(self):
        self.assertEqual(generate_email('Petr.Ivanov!!', 'gmail.com'), 'Petr.Ivanov__@gmail.com')

    def test_GenerateEmail_PercentSignInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(self):
        self.assertEqual(generate_email('Petr%Ivan%ov', 'gmail.com'), 'Petr_Ivan_ov@gmail.com')

    def test_GenerateEmail_DollarSignInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(self):
        self.assertEqual(generate_email('Petr$$Ivan$$ov', 'gmail.com'), 'Petr__Ivan__ov@gmail.com')

    def test_GenerateEmail_ExclamationAndPercentAndDollarSignInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(
            self):
        self.assertEqual(generate_email('Petr!Ivan%ov$', 'gmail.com'), 'Petr_Ivan_ov_@gmail.com')

    def test_GenerateEmail_questionMarkInLocalPart_EmailDoesNotReplaceWithExpectedCharacter(self):
        self.assertNotEqual(generate_email('Petr?', 'rambler.ru'), 'Petr_@rambler.ru')

    def test_GenerateEmail_NoUsernameInEmail_EmailNotCreated(self):
        self.assertNotEqual(generate_email(' ', 'gmail.com'), '@gmail.com')

    def test_GenerateEmail_NotValidEmptyDomainPart_EmailNotCreated(self):
        self.assertNotEqual(generate_email('PetrPetrov', ' '), 'PetrPetrov')

    def test_GenerateEmail_twoDotsInTheDomainName_EmailNotCreated(self):
        self.assertNotEqual(generate_email('PetrPetrov', 'gmail..com '), 'PetrPetrov@gmail..com')

