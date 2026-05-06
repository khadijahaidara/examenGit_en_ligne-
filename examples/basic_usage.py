"""
Exemple d'utilisation basique du projet examenGit_en_ligne
"""

from src.utils.functions import (
    factorielle, est_premier, generer_mot_de_passe, 
    fibonacci, calculer_imc, inverser_chaine
)
from src.game.game import JeuDevinette
from src.utils.logger import get_logger


def demo_functions():
    """Démonstration des fonctions utilitaires"""
    print("🔧 Démonstration des fonctions utilitaires")
    print("=" * 50)
    
    # Fonctions mathématiques
    print(f"Factorielle de 5: {factorielle(5)}")
    print(f"7 est-il premier? {est_premier(7)}")
    print(f"Suite de Fibonacci (10 termes): {fibonacci(10)}")
    print(f"IMC (70kg, 1.75m): {calculer_imc(70, 1.75)}")
    
    # Fonctions textuelles
    print(f"Inverser 'hello': '{inverser_chaine('hello')}'")
    print(f"Mot de passe généré: {generer_mot_de_passe(12)}")
    
    print("\n")


def demo_game_console():
    """Démonstration du jeu en console (simulation)"""
    print("🎮 Démonstration du jeu (simulation)")
    print("=" * 50)
    
    # Créer une instance du jeu
    game = JeuDevinette()
    
    # Afficher les statistiques initiales
    print("Statistiques initiales:")
    game.afficher_stats()
    
    print("\nPour jouer au jeu complet, exécutez:")
    print("python -m src.game.game")
    print("\n")


def demo_logging():
    """Démonstration du système de logging"""
    print("📝 Démonstration du système de logging")
    print("=" * 50)
    
    logger = get_logger()
    
    logger.info("Ceci est un message d'information")
    logger.warning("Ceci est un avertissement")
    logger.error("Ceci est une erreur")
    
    print("Messages de log envoyés. Vérifiez les fichiers de log.")
    print("\n")


def demo_advanced_usage():
    """Démonstration d'utilisation avancée"""
    print("🚀 Démonstration d'utilisation avancée")
    print("=" * 50)
    
    # Test de plusieurs fonctions avec gestion d'erreurs
    test_functions = [
        ("Factorielle", lambda: factorielle(6)),
        ("Nombre premier", lambda: est_premier(13)),
        ("PGCD", lambda: __import__('src.utils.functions', fromlist=['pgcd']).pgcd(24, 18)),
        ("Température", lambda: __import__('src.utils.functions', fromlist=['temperature_conversion']).temperature_conversion(25)),
    ]
    
    for name, func in test_functions:
        try:
            result = func()
            print(f"{name}: {result}")
        except Exception as e:
            print(f"{name}: Erreur - {e}")
    
    print("\n")


def main():
    """Fonction principale de démonstration"""
    print("🎯 EXEMPLES D'UTILISATION DU PROJET")
    print("=" * 60)
    
    try:
        demo_functions()
        demo_game_console()
        demo_logging()
        demo_advanced_usage()
        
        print("✅ Toutes les démonstrations ont été exécutées avec succès!")
        
    except Exception as e:
        print(f"❌ Erreur lors de la démonstration: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
