import unittest
from unittest.mock import MagicMock

# Dummy translator implementation for testing
class Translator:
    def translate(self, text):
        raise NotImplementedError

class MockTranslator:
    def translate(self, text):
        return f'Mock translation of {text}'

class TestTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = MockTranslator()

    def test_translate(self):
        text = 'Hello, world!'
        expected_translation = 'Mock translation of Hello, world!'
        self.assertEqual(self.translator.translate(text), expected_translation)

    def test_empty_translation(self):
        text = ''
        expected_translation = 'Mock translation of '
        self.assertEqual(self.translator.translate(text), expected_translation)

    def test_multiple_sentences(self):
        text = 'Hello. How are you?'
        expected_translation = 'Mock translation of Hello. How are you?'
        self.assertEqual(self.translator.translate(text), expected_translation)

if __name__ == '__main__':
    unittest.main()