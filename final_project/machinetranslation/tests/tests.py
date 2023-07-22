import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test2_thank_you(self):
        self.assertEqual(english_to_french('Thank you'), 'Merci')

class TestFrenchToEnglish(unittest.TestCase):
    def test1_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test2_merci(self):
        self.assertEqual(french_to_english('Merci'), 'Thank you')

    unittest.main()