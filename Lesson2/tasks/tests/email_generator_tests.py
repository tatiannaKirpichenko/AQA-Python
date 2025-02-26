import unittest

from Lesson2.tasks.src.email_generator import generate_email


class GenerateEmailTestCase(unittest.TestCase):

    def test_GenerateEmail_ValidLocalAndDomainParts_EmailGeneratedWithoutReplacement(self):
        local_part = 'Petr'

        domain_part = 'rambler.ru'

        generate_result = generate_email(local_part, domain_part)

        self.assertEqual('Petr@rambler.ru', generate_result)

    def test_GenerateEmail_ValidLocalPartsContainingDotAndDomainParts_EmailGeneratedWithoutReplacement(self):
        local_part = 'Petr.Ivanov'

        domain_part = 'gmail.com'

        generate_result = generate_email(local_part, domain_part)

        self.assertEqual('Petr.Ivanov@gmail.com', generate_result)

    def test_GenerateEmail_ExclamationMarkInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(self):
        local_part = 'Petr.Ivanov!!'

        domain_part = 'gmail.com'

        generate_result = generate_email(local_part, domain_part)

        self.assertEqual('Petr.Ivanov__@gmail.com', generate_result)

    def test_GenerateEmail_PercentSignInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(self):
        local_part = 'Petr%Ivan%ov'

        domain_part = 'gmail.com'

        generate_result = generate_email(local_part, domain_part)

        self.assertEqual('Petr_Ivan_ov@gmail.com', generate_result)

    def test_GenerateEmail_DollarSignInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(self):
        local_part = 'Petr$$Ivan$$ov'

        domain_part = 'gmail.com'

        generate_result = generate_email(local_part, domain_part)

        self.assertEqual('Petr__Ivan__ov@gmail.com', generate_result)

    def test_GenerateEmail_ExclamationAndPercentAndDollarSignInLocalPart_EmailGeneratedWithReplacementInvalidCharacters(
            self):
        local_part = 'Petr!Ivan%ov$'

        domain_part = 'gmail.com'

        generate_result = generate_email(local_part, domain_part)

        self.assertEqual('Petr_Ivan_ov_@gmail.com', generate_result)

    def test_GenerateEmail_questionMarkInLocalPart_EmailDoesNotReplaceWithExpectedCharacter(self):
        local_part = 'Petr?'

        domain_part = 'rambler.ru'

        generate_result = generate_email(local_part, domain_part)

        self.assertNotEqual('Petr_@rambler.ru', generate_result)

    def test_GenerateEmail_NoUsernameInEmail_EmailNotCreated(self):
        local_part = ' '

        domain_part = 'gmail.com'

        generate_result = generate_email(local_part, domain_part)

        self.assertNotEqual('@gmail.com', generate_result)

    def test_GenerateEmail_NotValidEmptyDomainPart_EmailNotCreated(self):
        local_part = 'PetrPetrov'

        domain_part = ' '

        generate_result = generate_email(local_part, domain_part)

        self.assertNotEqual('PetrPetrov', generate_result)
