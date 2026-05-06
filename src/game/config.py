"""
Configuration du jeu de devinette
"""

from dataclasses import dataclass
from typing import Tuple, Dict


@dataclass
class DifficultyLevel:
    """Représente un niveau de difficulté"""
    name: str
    max_number: int
    max_attempts: int
    description: str


class GameConfig:
    """Configuration centralisée du jeu"""
    
    DIFFICULTIES: Dict[str, DifficultyLevel] = {
        "1": DifficultyLevel(
            name="Facile",
            max_number=50,
            max_attempts=15,
            description="Niveau facile pour débuter"
        ),
        "2": DifficultyLevel(
            name="Moyen", 
            max_number=100,
            max_attempts=10,
            description="Niveau intermédiaire"
        ),
        "3": DifficultyLevel(
            name="Difficile",
            max_number=200,
            max_attempts=8,
            description="Niveau avancé"
        ),
        "4": DifficultyLevel(
            name="Expert",
            max_number=500,
            max_attempts=6,
            description="Niveau expert pour les pros"
        )
    }
    
    # Configuration des points
    POINTS_PER_ATTEMPT = 10
    MIN_POINTS = 10
    MAX_POINTS = 100
    
    # Messages du jeu
    MESSAGES = {
        "welcome": "🎮 JEU DE DEVINETTE DE NOMBRE 🎮",
        "win": "🎉 BRAVO! Vous avez trouvé le nombre",
        "lose": "😢 Dommage! Le nombre était",
        "higher": "📈 C'est plus grand!",
        "lower": "📉 C'est plus petit!",
        "very_hot": "🔥 Très chaud!",
        "hot": "♨️ Chaud!",
        "warm": "❄️ Tiède!",
        "cold": "🧊 Froid!",
        "invalid_input": "❌ Veuillez entrer un nombre valide.",
        "invalid_choice": "Choix invalide. Veuillez réessayer."
    }
    
    # Configuration de proximité
    PROXIMITY_THRESHOLDS = {
        "very_hot": 5,
        "hot": 10,
        "warm": 20
    }
    
    @classmethod
    def get_difficulty(cls, choice: str) -> DifficultyLevel:
        """
        Récupère un niveau de difficulté
        
        Args:
            choice (str): Choix de l'utilisateur (1-4)
            
        Returns:
            DifficultyLevel: Niveau de difficulté choisi
            
        Raises:
            ValueError: Si le choix n'est pas valide
        """
        if choice not in cls.DIFFICULTIES:
            raise ValueError("Choix de difficulté invalide")
        return cls.DIFFICULTIES[choice]
    
    @classmethod
    def calculate_points(cls, attempts: int, max_attempts: int) -> int:
        """
        Calcule les points gagnés selon le nombre d'essais
        
        Args:
            attempts (int): Nombre d'essais utilisés
            max_attempts (int): Nombre maximum d'essais
            
        Returns:
            int: Points gagnés
        """
        points = cls.MAX_POINTS - (attempts - 1) * cls.POINTS_PER_ATTEMPT
        return max(points, cls.MIN_POINTS)
    
    @classmethod
    def get_proximity_message(cls, difference: int) -> str:
        """
        Récupère le message de proximité selon la différence
        
        Args:
            difference (int): Différence absolue avec le nombre secret
            
        Returns:
            str: Message de proximité
        """
        if difference <= cls.PROXIMITY_THRESHOLDS["very_hot"]:
            return cls.MESSAGES["very_hot"]
        elif difference <= cls.PROXIMITY_THRESHOLDS["hot"]:
            return cls.MESSAGES["hot"]
        elif difference <= cls.PROXIMITY_THRESHOLDS["warm"]:
            return cls.MESSAGES["warm"]
        else:
            return cls.MESSAGES["cold"]
