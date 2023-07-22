import os
import sys
import unittest
import string

# Add the parent directory to the Python path to import the translator module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from machinetranslation.translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    def test_english_to_french_hello(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")

    def test_english_to_french_how_are_you(self):
        result = english_to_french("How are you?")
        self.assertEqual(result, "Comment ça va ?")

    def test_english_to_french_empty_string(self):
        # Test for an empty string
        result = english_to_french("")
        self.assertEqual(result, "")

    def test_english_to_french_special_characters(self):
        # Test for special characters
        result = english_to_french("@#$%^&*()")
        has_special_characters = any(char in string.ascii_letters for char in result)
        self.assertFalse(has_special_characters)

    def test_french_to_english_bonjour(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")

    def test_french_to_english_comment_ca_va(self):
        result = french_to_english("Comment ça va?")
        self.assertEqual(result, "How are you?")

    def test_french_to_english_empty_string(self):
        # Test for an empty string
        result = french_to_english("")
        self.assertEqual(result, "")

    def test_french_to_english_special_characters(self):
        # Test for special characters
        result = french_to_english("@#$%^&*()")
        has_special_characters = any(char in string.ascii_letters for char in result)
        self.assertFalse(has_special_characters)


    unittest.main()
