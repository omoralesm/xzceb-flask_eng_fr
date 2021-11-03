"""
Test translation
"""
import unittest

from ibm_watson import ApiException

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Test translation from english to french
    """
    def test1(self):
        """
        Test translation cases
        """
        self.assertEqual(english_to_french("Red"), "Rouge")
        self.assertEqual(english_to_french("Car"), "Voiture")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        with self.assertRaises(ApiException):
            english_to_french("")
        

class TestFrenchToEnglish(unittest.TestCase):
    """
    Test translation from french to english
    """
    def test1(self):
        """
        Test translation cases
        """
        self.assertEqual(french_to_english("Rouge"), "Red")
        self.assertEqual(french_to_english("Voiture"), "Car")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        with self.assertRaises(ApiException):
            french_to_english("")

        
unittest.main()
