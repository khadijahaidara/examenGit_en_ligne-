"""
Tests complets pour les fonctions utilitaires
"""

import unittest
import math
import random
import string
from src.utils.functions import (
    factorielle,
    est_premier,
    generer_mot_de_passe,
    fibonacci,
    calculer_imc,
    inverser_chaine,
    compter_voyelles,
    temperature_conversion,
    pgcd,
    format_temps
)


class TestFactorielle(unittest.TestCase):
    """Tests pour la fonction factorielle"""
    
    def test_factorielle_cas_normaux(self):
        """Test les cas normaux de factorielle"""
        self.assertEqual(factorielle(0), 1)
        self.assertEqual(factorielle(1), 1)
        self.assertEqual(factorielle(5), 120)
        self.assertEqual(factorielle(6), 720)
        self.assertEqual(factorielle(10), 3628800)
    
    def test_factorielle_erreur_negatif(self):
        """Test que factorielle lève une erreur pour les nombres négatifs"""
        with self.assertRaises(ValueError):
            factorielle(-1)
        with self.assertRaises(ValueError):
            factorielle(-10)
    
    def test_factorielle_performance(self):
        """Test les performances pour des nombres plus grands"""
        # Test que ça fonctionne pour des nombres raisonnables
        self.assertEqual(factorielle(12), 479001600)


class TestEstPremier(unittest.TestCase):
    """Tests pour la fonction est_premier"""
    
    def test_est_premier_cas_normaux(self):
        """Test les cas normaux pour les nombres premiers"""
        self.assertFalse(est_premier(1))
        self.assertTrue(est_premier(2))
        self.assertTrue(est_premier(3))
        self.assertFalse(est_premier(4))
        self.assertTrue(est_premier(5))
        self.assertFalse(est_premier(6))
        self.assertTrue(est_premier(7))
        self.assertFalse(est_premier(8))
        self.assertFalse(est_premier(9))
        self.assertTrue(est_premier(11))
        self.assertTrue(est_premier(13))
        self.assertFalse(est_premier(15))
    
    def test_est_premier_grands_nombres(self):
        """Test avec des nombres plus grands"""
        self.assertTrue(est_premier(97))
        self.assertTrue(est_premier(101))
        self.assertFalse(est_premier(100))
        self.assertFalse(est_premier(99))
    
    def test_est_premier_zero_et_negatif(self):
        """Test avec zéro et nombres négatifs"""
        self.assertFalse(est_premier(0))
        self.assertFalse(est_premier(-1))
        self.assertFalse(est_premier(-10))


class TestGenererMotDePasse(unittest.TestCase):
    """Tests pour la fonction generer_mot_de_passe"""
    
    def test_generer_mot_de_passe_longueur_par_defaut(self):
        """Test la génération avec la longueur par défaut"""
        password = generer_mot_de_passe()
        self.assertEqual(len(password), 12)
        self.assertTrue(all(c in string.ascii_letters + string.digits + "!@#$%^&*" for c in password))
    
    def test_generer_mot_de_passe_longueur_personnalisee(self):
        """Test la génération avec des longueurs personnalisées"""
        for length in [4, 8, 16, 20]:
            password = generer_mot_de_passe(length)
            self.assertEqual(len(password), length)
    
    def test_generer_mot_de_passe_erreur_longueur_minimale(self):
        """Test que la fonction lève une erreur pour les longueurs trop courtes"""
        with self.assertRaises(ValueError):
            generer_mot_de_passe(3)
        with self.assertRaises(ValueError):
            generer_mot_de_passe(0)
    
    def test_generer_mot_de_passe_unicite(self):
        """Test que les mots de passe générés sont uniques"""
        passwords = [generer_mot_de_passe(8) for _ in range(10)]
        self.assertEqual(len(set(passwords)), 10)  # Tous différents


class TestFibonacci(unittest.TestCase):
    """Tests pour la fonction fibonacci"""
    
    def test_fibonacci_cas_normaux(self):
        """Test les cas normaux de fibonacci"""
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    
    def test_fibonacci_erreur_negatif(self):
        """Test que fibonacci lève une erreur pour les nombres négatifs"""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-5)
    
    def test_fibonacci_performance(self):
        """Test les performances pour des séquences plus longues"""
        sequence = fibonacci(20)
        self.assertEqual(len(sequence), 20)
        self.assertEqual(sequence[-1], 4181)  # 19ème terme de fibonacci


class TestCalculerIMC(unittest.TestCase):
    """Tests pour la fonction calculer_imc"""
    
    def test_calculer_imc_cas_normaux(self):
        """Test les cas normaux de calcul IMC"""
        self.assertAlmostEqual(calculer_imc(70, 1.75), 22.86, places=2)
        self.assertAlmostEqual(calculer_imc(60, 1.65), 22.04, places=2)
        self.assertAlmostEqual(calculer_imc(80, 1.80), 24.69, places=2)
        self.assertAlmostEqual(calculer_imc(50, 1.60), 19.53, places=2)
    
    def test_calculer_imc_erreur_taille(self):
        """Test que calculer_imc lève une erreur pour les tailles invalides"""
        with self.assertRaises(ValueError):
            calculer_imc(70, 0)
        with self.assertRaises(ValueError):
            calculer_imc(70, -1.75)
    
    def test_calculer_imc_poids_negatif(self):
        """Test avec un poids négatif (devrait fonctionner mathématiquement)"""
        result = calculer_imc(-70, 1.75)
        self.assertAlmostEqual(result, -22.86, places=2)


class TestInverserChaine(unittest.TestCase):
    """Tests pour la fonction inverser_chaine"""
    
    def test_inverser_chaine_cas_normaux(self):
        """Test les cas normaux d'inversion de chaîne"""
        self.assertEqual(inverser_chaine("hello"), "olleh")
        self.assertEqual(inverser_chaine("Python"), "nohtyP")
        self.assertEqual(inverser_chaine(""), "")
        self.assertEqual(inverser_chaine("a"), "a")
        self.assertEqual(inverser_chaine("12345"), "54321")
    
    def test_inverser_chaine_avec_espaces(self):
        """Test l'inversion avec des espaces et caractères spéciaux"""
        self.assertEqual(inverser_chaine("hello world"), "dlrow olleh")
        self.assertEqual(inverser_chaine("123 456"), "654 321")
        self.assertEqual(inverser_chaine("!@#$"), "$#@!")
    
    def test_inverser_chaine_unicode(self):
        """Test avec des caractères unicode"""
        self.assertEqual(inverser_chaine("café"), "éfac")
        self.assertEqual(inverser_chaine("naïve"), "evïan")


class TestCompterVoyelles(unittest.TestCase):
    """Tests pour la fonction compter_voyelles"""
    
    def test_compter_voyelles_cas_normaux(self):
        """Test les cas normaux de comptage de voyelles"""
        self.assertEqual(compter_voyelles("hello"), 2)
        self.assertEqual(compter_voyelles("python"), 1)
        self.assertEqual(compter_voyelles("aeiou"), 5)
        self.assertEqual(compter_voyelles("bcdfg"), 0)
        self.assertEqual(compter_voyelles(""), 0)
    
    def test_compter_voyelles_majuscules(self):
        """Test avec des majuscules"""
        self.assertEqual(compter_voyelles("HELLO"), 2)
        self.assertEqual(compter_voyelles("AEIOU"), 5)
        self.assertEqual(compter_voyelles("Python"), 1)
    
    def test_compter_voyelles_avec_espaces(self):
        """Test avec des espaces et ponctuation"""
        self.assertEqual(compter_voyelles("hello world"), 3)
        self.assertEqual(compter_voyelles("python, c'est cool!"), 5)
    
    def test_compter_voyelles_erreur_type(self):
        """Test que la fonction lève une erreur pour les types invalides"""
        with self.assertRaises(ValueError):
            compter_voyelles(123)
        with self.assertRaises(ValueError):
            compter_voyelles(None)
        with self.assertRaises(ValueError):
            compter_voyelles(["hello"])


class TestTemperatureConversion(unittest.TestCase):
    """Tests pour la fonction temperature_conversion"""
    
    def test_temperature_conversion_vers_fahrenheit(self):
        """Test la conversion vers Fahrenheit"""
        self.assertAlmostEqual(temperature_conversion(0), 32, places=2)
        self.assertAlmostEqual(temperature_conversion(100), 212, places=2)
        self.assertAlmostEqual(temperature_conversion(-40), -40, places=2)
        self.assertAlmostEqual(temperature_conversion(37), 98.6, places=2)
    
    def test_temperature_conversion_vers_celsius(self):
        """Test la conversion vers Celsius"""
        self.assertAlmostEqual(temperature_conversion(32, False), 0, places=2)
        self.assertAlmostEqual(temperature_conversion(212, False), 100, places=2)
        self.assertAlmostEqual(temperature_conversion(-40, False), -40, places=2)
        self.assertAlmostEqual(temperature_conversion(98.6, False), 37, places=2)
    
    def test_temperature_conversion_negatifs(self):
        """Test avec des températures négatives"""
        self.assertAlmostEqual(temperature_conversion(-10), 14, places=2)
        self.assertAlmostEqual(temperature_conversion(14, False), -10, places=2)


class TestPGCD(unittest.TestCase):
    """Tests pour la fonction pgcd"""
    
    def test_pgcd_cas_normaux(self):
        """Test les cas normaux de PGCD"""
        self.assertEqual(pgcd(12, 18), 6)
        self.assertEqual(pgcd(8, 12), 4)
        self.assertEqual(pgcd(17, 23), 1)
        self.assertEqual(pgcd(100, 25), 25)
        self.assertEqual(pgcd(0, 5), 5)
        self.assertEqual(pgcd(5, 0), 5)
    
    def test_pgcd_negatifs(self):
        """Test avec des nombres négatifs"""
        self.assertEqual(pgcd(-12, 18), 6)
        self.assertEqual(pgcd(12, -18), 6)
        self.assertEqual(pgcd(-12, -18), 6)
    
    def test_pgcd_zero(self):
        """Test avec zéro"""
        self.assertEqual(pgcd(0, 0), 0)
        self.assertEqual(pgcd(0, 1), 1)
        self.assertEqual(pgcd(1, 0), 1)
    
    def test_pgcd_nombres_premiers(self):
        """Test avec des nombres premiers"""
        self.assertEqual(pgcd(13, 17), 1)
        self.assertEqual(pgcd(7, 11), 1)


class TestFormatTemps(unittest.TestCase):
    """Tests pour la fonction format_temps"""
    
    def test_format_temps_cas_normaux(self):
        """Test les cas normaux de formatage de temps"""
        self.assertEqual(format_temps(0), "00:00:00")
        self.assertEqual(format_temps(1), "00:00:01")
        self.assertEqual(format_temps(60), "00:01:00")
        self.assertEqual(format_temps(3600), "01:00:00")
        self.assertEqual(format_temps(3661), "01:01:01")
        self.assertEqual(format_temps(86400), "24:00:00")
    
    def test_format_temps_grandes_valeurs(self):
        """Test avec des valeurs plus grandes"""
        self.assertEqual(format_temps(90061), "25:01:01")  # Plus de 24h
        self.assertEqual(format_temps(123456), "34:17:36")
    
    def test_format_temps_erreur_negatif(self):
        """Test que format_temps lève une erreur pour les valeurs négatives"""
        with self.assertRaises(ValueError):
            format_temps(-1)
        with self.assertRaises(ValueError):
            format_temps(-60)


if __name__ == '__main__':
    unittest.main()
