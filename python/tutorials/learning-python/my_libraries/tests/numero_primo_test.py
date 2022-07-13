import unittest
from ..numero_primo import is_primo
import pytest

class TestNumeroPrimo(unittest.TestCase):

    def test_negativo(self):
        self.assertRaises(ValueError,is_primo,number=-1)

    def test_positivo(self):
        self.assertEqual(is_primo(1), True)
        self.assertEqual(is_primo(2), True)
        self.assertEqual(is_primo(3), True)
        self.assertEqual(is_primo(4), False)
        self.assertEqual(is_primo(5), True)
        self.assertEqual(is_primo(6), False)
        self.assertEqual(is_primo(7), True)
        self.assertEqual(is_primo(8), False)
        self.assertEqual(is_primo(9), False)
        self.assertEqual(is_primo(10), False)
        self.assertEqual(is_primo(11), True)
        self.assertEqual(is_primo(12), False)
        self.assertEqual(is_primo(13), True)
        self.assertEqual(is_primo(89), True)
        self.assertEqual(is_primo(90), False)
        self.assertEqual(is_primo(433494437),True)
        
    def test_exception_raised_when_negative_value(self):
        with pytest.raises(ValueError):
            is_primo(-1)
        