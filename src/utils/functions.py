"""
Module contenant des fonctions utilitaires mathématiques et textuelles
"""

import math
import random
import string
from datetime import datetime


def factorielle(n):
    """
    Calcule la factorielle d'un nombre n
    
    Args:
        n (int): Nombre dont on veut calculer la factorielle
        
    Returns:
        int: La factorielle de n
        
    Raises:
        ValueError: Si n est négatif
        
    Examples:
        >>> factorielle(5)
        120
        >>> factorielle(0)
        1
    """
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs")
    if n == 0 or n == 1:
        return 1
    return n * factorielle(n - 1)


def est_premier(nombre):
    """
    Vérifie si un nombre est premier
    
    Args:
        nombre (int): Nombre à vérifier
        
    Returns:
        bool: True si le nombre est premier, False sinon
        
    Examples:
        >>> est_premier(7)
        True
        >>> est_premier(4)
        False
    """
    if nombre < 2:
        return False
    for i in range(2, int(math.sqrt(nombre)) + 1):
        if nombre % i == 0:
            return False
    return True


def generer_mot_de_passe(longueur=12):
    """
    Génère un mot de passe aléatoire sécurisé
    
    Args:
        longueur (int): Longueur du mot de passe (défaut: 12)
        
    Returns:
        str: Mot de passe généré
        
    Examples:
        >>> len(generer_mot_de_passe(8))
        8
    """
    if longueur < 4:
        raise ValueError("La longueur minimale est de 4 caractères")
    
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(caracteres) for _ in range(longueur))


def fibonacci(n):
    """
    Génère la suite de Fibonacci jusqu'à n termes
    
    Args:
        n (int): Nombre de termes à générer
        
    Returns:
        list: Liste contenant les n premiers termes de Fibonacci
        
    Examples:
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
    """
    if n < 0:
        raise ValueError("Le nombre de termes ne peut être négatif")
    
    suite = []
    a, b = 0, 1
    for _ in range(n):
        suite.append(a)
        a, b = b, a + b
    return suite


def calculer_imc(poids, taille):
    """
    Calcule l'Indice de Masse Corporelle (IMC)
    
    Args:
        poids (float): Poids en kg
        taille (float): Taille en mètres
        
    Returns:
        float: IMC arrondi à 2 décimales
        
    Raises:
        ValueError: Si la taille est négative ou nulle
        
    Examples:
        >>> calculer_imc(70, 1.75)
        22.86
    """
    if taille <= 0:
        raise ValueError("La taille doit être positive")
    return round(poids / (taille ** 2), 2)


def inverser_chaine(chaine):
    """
    Inverse une chaîne de caractères
    
    Args:
        chaine (str): Chaîne à inverser
        
    Returns:
        str: Chaîne inversée
        
    Examples:
        >>> inverser_chaine("hello")
        'olleh'
    """
    return chaine[::-1]


def compter_voyelles(texte):
    """
    Compte le nombre de voyelles dans un texte
    
    Args:
        texte (str): Texte à analyser
        
    Returns:
        int: Nombre de voyelles
        
    Examples:
        >>> compter_voyelles("hello")
        2
    """
    if not isinstance(texte, str):
        raise ValueError("L'entrée doit être une chaîne de caractères")
    
    voyelles = "aeiouAEIOU"
    return sum(1 for char in texte if char in voyelles)


def temperature_conversion(celsius, vers_fahrenheit=True):
    """
    Convertit les températures entre Celsius et Fahrenheit
    
    Args:
        celsius (float): Température en Celsius
        vers_fahrenheit (bool): Si True, convertit vers Fahrenheit, sinon vers Celsius
        
    Returns:
        float: Température convertie
        
    Examples:
        >>> round(temperature_conversion(0), 1)
        32.0
    """
    if vers_fahrenheit:
        return (celsius * 9/5) + 32
    else:
        return (celsius - 32) * 5/9


def pgcd(a, b):
    """
    Calcule le Plus Grand Commun Diviseur de deux nombres
    
    Args:
        a (int): Premier nombre
        b (int): Deuxième nombre
        
    Returns:
        int: PGCD des deux nombres
        
    Examples:
        >>> pgcd(12, 18)
        6
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def format_temps(secondes):
    """
    Convertit des secondes en format heures:minutes:secondes
    
    Args:
        secondes (int): Nombre de secondes
        
    Returns:
        str: Temps formaté HH:MM:SS
        
    Examples:
        >>> format_temps(3661)
        '01:01:01'
    """
    if secondes < 0:
        raise ValueError("Le nombre de secondes ne peut être négatif")
    
    heures = secondes // 3600
    minutes = (secondes % 3600) // 60
    secondes_restantes = secondes % 60
    return f"{heures:02d}:{minutes:02d}:{secondes_restantes:02d}"
