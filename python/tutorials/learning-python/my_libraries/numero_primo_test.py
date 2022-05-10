import unittest
import numero_primo as np
import pytest

class TestNumeroPrimo(unittest.TestCase):

    def test_negativo(self):
        self.assertRaises(ValueError,np.is_primo,number=-1)

    def test_positivo(self):
        self.assertEqual(np.is_primo(1), True)
        self.assertEqual(np.is_primo(2), True)
        self.assertEqual(np.is_primo(3), True)
        self.assertEqual(np.is_primo(4), False)
        self.assertEqual(np.is_primo(5), True)
        self.assertEqual(np.is_primo(6), False)
        self.assertEqual(np.is_primo(7), True)
        self.assertEqual(np.is_primo(8), False)
        self.assertEqual(np.is_primo(9), False)
        self.assertEqual(np.is_primo(10), False)
        self.assertEqual(np.is_primo(11), True)
        
    def test_exception_raised_when_negative_value(self):
        with pytest.raises(ValueError):
            np.is_primo(-1)
        