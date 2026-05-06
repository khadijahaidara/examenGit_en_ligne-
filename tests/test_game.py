"""
Tests pour le module de jeu
"""

import unittest
import json
import tempfile
import os
from unittest.mock import patch, MagicMock
from src.game.game import JeuDevinette, GameStats
from src.game.config import GameConfig


class TestGameConfig(unittest.TestCase):
    """Tests pour la configuration du jeu"""
    
    def test_get_difficulty_valid(self):
        """Test la récupération de difficultés valides"""
        easy = GameConfig.get_difficulty("1")
        self.assertEqual(easy.name, "Facile")
        self.assertEqual(easy.max_number, 50)
        self.assertEqual(easy.max_attempts, 15)
        
        expert = GameConfig.get_difficulty("4")
        self.assertEqual(expert.name, "Expert")
        self.assertEqual(expert.max_number, 500)
        self.assertEqual(expert.max_attempts, 6)
    
    def test_get_difficulty_invalid(self):
        """Test que les difficultés invalides lèvent une erreur"""
        with self.assertRaises(ValueError):
            GameConfig.get_difficulty("0")
        with self.assertRaises(ValueError):
            GameConfig.get_difficulty("5")
        with self.assertRaises(ValueError):
            GameConfig.get_difficulty("invalid")
    
    def test_calculate_points(self):
        """Test le calcul des points"""
        # Test avec le nombre maximum de points
        points = GameConfig.calculate_points(1, 10)
        self.assertEqual(points, 100)
        
        # Test avec le nombre minimum de points
        points = GameConfig.calculate_points(10, 10)
        self.assertEqual(points, 10)
        
        # Test avec un nombre intermédiaire
        points = GameConfig.calculate_points(5, 10)
        self.assertEqual(points, 60)
    
    def test_get_proximity_message(self):
        """Test les messages de proximité"""
        self.assertEqual(GameConfig.get_proximity_message(3), "🔥 Très chaud!")
        self.assertEqual(GameConfig.get_proximity_message(8), "♨️ Chaud!")
        self.assertEqual(GameConfig.get_proximity_message(15), "❄️ Tiède!")
        self.assertEqual(GameConfig.get_proximity_message(25), "🧊 Froid!")


class TestGameStats(unittest.TestCase):
    """Tests pour la classe GameStats"""
    
    def setUp(self):
        """Configuration pour chaque test"""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        self.stats = GameStats(self.temp_file.name)
    
    def tearDown(self):
        """Nettoyage après chaque test"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_initial_stats(self):
        """Test les statistiques initiales"""
        self.assertEqual(self.stats.stats["total_games"], 0)
        self.assertEqual(self.stats.stats["games_won"], 0)
        self.assertEqual(self.stats.stats["total_score"], 0)
        self.assertEqual(self.stats.stats["best_score"], 0)
    
    def test_update_game_win(self):
        """Test la mise à jour après une victoire"""
        self.stats.update_game(True, 50, 3, "Facile")
        
        self.assertEqual(self.stats.stats["total_games"], 1)
        self.assertEqual(self.stats.stats["games_won"], 1)
        self.assertEqual(self.stats.stats["total_score"], 50)
        self.assertEqual(self.stats.stats["best_score"], 50)
        self.assertEqual(self.stats.stats["average_attempts"], 3.0)
    
    def test_update_game_lose(self):
        """Test la mise à jour après une défaite"""
        self.stats.update_game(False, 0, 8, "Expert")
        
        self.assertEqual(self.stats.stats["total_games"], 1)
        self.assertEqual(self.stats.stats["games_won"], 0)
        self.assertEqual(self.stats.stats["total_score"], 0)
        self.assertEqual(self.stats.stats["best_score"], 0)
        self.assertEqual(self.stats.stats["average_attempts"], 8.0)
    
    def test_win_rate(self):
        """Test le calcul du taux de réussite"""
        # 0 parties jouées
        self.assertEqual(self.stats.get_win_rate(), 0.0)
        
        # 1 victoire sur 1 partie
        self.stats.update_game(True, 100, 1, "Facile")
        self.assertEqual(self.stats.get_win_rate(), 100.0)
        
        # 1 victoire sur 2 parties
        self.stats.update_game(False, 0, 10, "Expert")
        self.assertEqual(self.stats.get_win_rate(), 50.0)
    
    def test_difficulty_stats(self):
        """Test les statistiques par difficulté"""
        self.stats.update_game(True, 50, 3, "Facile")
        self.stats.update_game(False, 0, 8, "Facile")
        self.stats.update_game(True, 80, 2, "Expert")
        
        facile_stats = self.stats.stats["difficulty_stats"]["Facile"]
        self.assertEqual(facile_stats["games"], 2)
        self.assertEqual(facile_stats["wins"], 1)
        
        expert_stats = self.stats.stats["difficulty_stats"]["Expert"]
        self.assertEqual(expert_stats["games"], 1)
        self.assertEqual(expert_stats["wins"], 1)
    
    def test_save_and_load(self):
        """Test la sauvegarde et le chargement des statistiques"""
        # Mise à jour des stats
        self.stats.update_game(True, 100, 1, "Facile")
        
        # Création d'une nouvelle instance avec le même fichier
        new_stats = GameStats(self.temp_file.name)
        
        # Vérification que les stats ont été chargées
        self.assertEqual(new_stats.stats["total_games"], 1)
        self.assertEqual(new_stats.stats["games_won"], 1)
        self.assertEqual(new_stats.stats["total_score"], 100)


class TestJeuDevinette(unittest.TestCase):
    """Tests pour la classe JeuDevinette"""
    
    def setUp(self):
        """Configuration pour chaque test"""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        self.game = JeuDevinette(self.temp_file.name)
    
    def tearDown(self):
        """Nettoyage après chaque test"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_initialization(self):
        """Test l'initialisation du jeu"""
        self.assertIsNotNone(self.game.stats)
        self.assertEqual(self.game.score, 0)
        self.assertIsNone(self.game.current_difficulty)
    
    @patch('builtins.input')
    def test_choisir_difficulte_valid(self, mock_input):
        """Test le choix d'une difficulté valide"""
        mock_input.return_value = "2"
        difficulty = self.game.choisir_difficulte()
        
        self.assertEqual(difficulty.name, "Moyen")
        self.assertEqual(difficulty.max_number, 100)
        self.assertEqual(difficulty.max_attempts, 10)
    
    @patch('builtins.input')
    def test_choisir_difficulte_invalid_then_valid(self, mock_input):
        """Test le choix d'une difficulté invalide puis valide"""
        mock_input.side_effect = ["0", "3"]
        difficulty = self.game.choisir_difficulte()
        
        self.assertEqual(difficulty.name, "Difficile")
        self.assertEqual(difficulty.max_number, 200)
    
    @patch('builtins.input')
    @patch('random.randint')
    def test_jouer_partie_win(self, mock_randint, mock_input):
        """Test une partie gagnée"""
        # Configuration du mock
        mock_randint.return_value = 42
        mock_input.side_effect = ["2", "42"]  # Difficulté moyenne, puis la bonne réponse
        
        result = self.game.jouer_partie()
        
        self.assertTrue(result)
        self.assertEqual(self.game.score, 100)  # 100 points pour 1 essai
        self.assertEqual(self.game.stats.stats["total_games"], 1)
        self.assertEqual(self.game.stats.stats["games_won"], 1)
    
    @patch('builtins.input')
    @patch('random.randint')
    def test_jouer_partie_lose(self, mock_randint, mock_input):
        """Test une partie perdue"""
        # Configuration du mock
        mock_randint.return_value = 42
        # Difficulté facile (15 essais max), puis 15 mauvaises réponses
        mock_input.side_effect = ["1"] + ["1"] * 15
        
        result = self.game.jouer_partie()
        
        self.assertFalse(result)
        self.assertEqual(self.game.stats.stats["total_games"], 1)
        self.assertEqual(self.game.stats.stats["games_won"], 0)
    
    @patch('builtins.input')
    @patch('random.randint')
    def test_jouer_partie_multiple_attempts(self, mock_randint, mock_input):
        """Test une partie avec plusieurs essais"""
        mock_randint.return_value = 42
        mock_input.side_effect = ["2", "30", "40", "42"]  # Difficulté moyenne, 3 essais
        
        result = self.game.jouer_partie()
        
        self.assertTrue(result)
        self.assertEqual(self.game.score, 80)  # 100 - 2*10
        self.assertEqual(self.game.attempts, 3)
    
    def test_handle_win(self):
        """Test la gestion d'une victoire"""
        from src.game.config import DifficultyLevel
        
        difficulty = DifficultyLevel("Test", 100, 10, "Test difficulty")
        result = self.game._handle_win(difficulty)
        
        self.assertTrue(result)
        self.assertGreater(self.game.score, 0)
        self.assertEqual(self.game.stats.stats["games_won"], 1)
    
    def test_handle_lose(self):
        """Test la gestion d'une défaite"""
        self.game.current_difficulty = MagicMock()
        self.game.current_difficulty.name = "Test"
        
        result = self.game._handle_lose()
        
        self.assertFalse(result)
        self.assertEqual(self.game.stats.stats["games_won"], 0)
    
    def test_handle_wrong_guess(self):
        """Test la gestion des mauvaises propositions"""
        self.game.secret_number = 42
        
        # Test proposition plus petite
        self.game._handle_wrong_guess(30)
        # Test proposition plus grande
        self.game._handle_wrong_guess(50)
        
        # Pas d'exception levée
        self.assertTrue(True)


class TestIntegration(unittest.TestCase):
    """Tests d'intégration"""
    
    def setUp(self):
        """Configuration pour chaque test"""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
    
    def tearDown(self):
        """Nettoyage après chaque test"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    @patch('builtins.input')
    def test_complete_game_flow(self, mock_input):
        """Test un flux de jeu complet"""
        # Simuler une partie complète
        mock_input.side_effect = [
            "1",  # Jouer une partie
            "1",  # Difficulté facile
            "25", "30", "35", "40", "45", "50",  # Propositions
            "4"   # Quitter
        ]
        
        game = JeuDevinette(self.temp_file.name)
        
        # Simuler le nombre secret
        with patch('random.randint', return_value=50):
            with patch('time.sleep'):  # Ignorer les pauses
                try:
                    game.menu_principal()
                except SystemExit:
                    pass  # Sortie normale du jeu
        
        # Vérifier que les stats ont été mises à jour
        self.assertGreater(game.stats.stats["total_games"], 0)


if __name__ == '__main__':
    unittest.main()
