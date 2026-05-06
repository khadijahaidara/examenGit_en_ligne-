import unittest
import math
from mesfonctions import factorielle, est_premier, fibonacci, calculer_imc, inverser_chaine

class TestMesFonctions(unittest.TestCase):
    
    def test_factorielle(self):
        """Test la fonction factorielle"""
        self.assertEqual(factorielle(0), 1)
        self.assertEqual(factorielle(1), 1)
        self.assertEqual(factorielle(5), 120)
        self.assertEqual(factorielle(6), 720)
        with self.assertRaises(ValueError):
            factorielle(-1)
    
    def test_est_premier(self):
        """Test la fonction est_premier"""
        self.assertFalse(est_premier(1))
        self.assertTrue(est_premier(2))
        self.assertTrue(est_premier(3))
        self.assertFalse(est_premier(4))
        self.assertTrue(est_premier(5))
        self.assertFalse(est_premier(6))
        self.assertTrue(est_premier(7))
        self.assertFalse(est_premier(9))
        self.assertTrue(est_premier(13))
        self.assertFalse(est_premier(15))
    
    def test_fibonacci(self):
        """Test la fonction fibonacci"""
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    
    def test_calculer_imc(self):
        """Test la fonction calculer_imc"""
        self.assertAlmostEqual(calculer_imc(70, 1.75), 22.86, places=2)
        self.assertAlmostEqual(calculer_imc(60, 1.65), 22.04, places=2)
        self.assertAlmostEqual(calculer_imc(80, 1.80), 24.69, places=2)
        with self.assertRaises(ValueError):
            calculer_imc(70, 0)
        with self.assertRaises(ValueError):
            calculer_imc(70, -1.75)
    
    def test_inverser_chaine(self):
        """Test la fonction inverser_chaine"""
        self.assertEqual(inverser_chaine("hello"), "olleh")
        self.assertEqual(inverser_chaine("Python"), "nohtyP")
        self.assertEqual(inverser_chaine(""), "")
        self.assertEqual(inverser_chaine("a"), "a")
        self.assertEqual(inverser_chaine("12345"), "54321")

if __name__ == '__main__':
    unittest.main()
