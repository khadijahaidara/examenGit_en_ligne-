<!--premiere ligne-->

import math
import random
import string
from datetime import datetime

def factorielle(n):
    """Calcule la factorielle d'un nombre n"""
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs")
    if n == 0 or n == 1:
        return 1
    return n * factorielle(n - 1)

def est_premier(nombre):
    """Vérifie si un nombre est premier"""
    if nombre < 2:
        return False
    for i in range(2, int(math.sqrt(nombre)) + 1):
        if nombre % i == 0:
            return False
    return True

def generer_mot_de_passe(longueur=12):
    """Génère un mot de passe aléatoire sécurisé"""
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(caracteres) for _ in range(longueur))

def fibonacci(n):
    """Génère la suite de Fibonacci jusqu'à n termes"""
    suite = []
    a, b = 0, 1
    for _ in range(n):
        suite.append(a)
        a, b = b, a + b
    return suite

def calculer_imc(poids, taille):
    """Calcule l'Indice de Masse Corporelle (IMC)"""
    if taille <= 0:
        raise ValueError("La taille doit être positive")
    return round(poids / (taille ** 2), 2)

def inverser_chaine(chaine):
    """Inverse une chaîne de caractères"""
    return chaine[::-1]

def compter_voyelles(texte):
    """Compte le nombre de voyelles dans un texte"""
    voyelles = "aeiouAEIOU"
    return sum(1 for char in texte if char in voyelles)

def temperature_conversion(celsius, vers_fahrenheit=True):
    """Convertit les températures entre Celsius et Fahrenheit"""
    if vers_fahrenheit:
        return (celsius * 9/5) + 32
    else:
        return (celsius - 32) * 5/9

def pgcd(a, b):
    """Calcule le Plus Grand Commun Diviseur de deux nombres"""
    while b:
        a, b = b, a % b
    return a

def format_temps(secondes):
    """Convertit des secondes en format heures:minutes:secondes"""
    heures = secondes // 3600
    minutes = (secondes % 3600) // 60
    secondes_restantes = secondes % 60
    return f"{heures:02d}:{minutes:02d}:{secondes_restantes:02d}"
