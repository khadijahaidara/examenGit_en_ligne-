"""
Module principal du jeu de devinette
"""

import random
import time
import os
import json
from typing import Optional, Dict, Any
from datetime import datetime

from .config import GameConfig, DifficultyLevel
from ..utils.logger import get_logger


class GameStats:
    """Classe pour gérer les statistiques du joueur"""
    
    def __init__(self, stats_file: str = "game_stats.json"):
        self.stats_file = stats_file
        self.stats = self._load_stats()
    
    def _load_stats(self) -> Dict[str, Any]:
        """Charge les statistiques depuis le fichier"""
        try:
            with open(self.stats_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                "total_games": 0,
                "games_won": 0,
                "total_score": 0,
                "best_score": 0,
                "average_attempts": 0,
                "last_played": None,
                "difficulty_stats": {}
            }
    
    def save_stats(self):
        """Sauvegarde les statistiques dans le fichier"""
        self.stats["last_played"] = datetime.now().isoformat()
        try:
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, indent=2, ensure_ascii=False)
        except Exception as e:
            get_logger().error(f"Erreur lors de la sauvegarde des stats: {e}")
    
    def update_game(self, won: bool, score: int, attempts: int, difficulty: str):
        """Met à jour les statistiques après une partie"""
        self.stats["total_games"] += 1
        if won:
            self.stats["games_won"] += 1
            self.stats["total_score"] += score
            if score > self.stats["best_score"]:
                self.stats["best_score"] = score
        
        # Mise à jour de la moyenne d'essais
        total_attempts = self.stats.get("total_attempts", 0) + attempts
        self.stats["total_attempts"] = total_attempts
        self.stats["average_attempts"] = total_attempts / self.stats["total_games"]
        
        # Statistiques par difficulté
        if difficulty not in self.stats["difficulty_stats"]:
            self.stats["difficulty_stats"][difficulty] = {
                "games": 0,
                "wins": 0
            }
        self.stats["difficulty_stats"][difficulty]["games"] += 1
        if won:
            self.stats["difficulty_stats"][difficulty]["wins"] += 1
        
        self.save_stats()
    
    def get_win_rate(self) -> float:
        """Calcule le taux de réussite"""
        if self.stats["total_games"] == 0:
            return 0.0
        return (self.stats["games_won"] / self.stats["total_games"]) * 100


class JeuDevinette:
    """Jeu de devinette de nombre avec niveaux de difficulté"""
    
    def __init__(self, stats_file: Optional[str] = None):
        self.logger = get_logger()
        self.stats = GameStats(stats_file) if stats_file else GameStats()
        self.score = 0
        self.current_difficulty: Optional[DifficultyLevel] = None
        self.secret_number = 0
        self.attempts = 0
        
    def effacer_ecran(self):
        """Efface l'écran de la console"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def afficher_titre(self):
        """Affiche le titre du jeu avec les statistiques actuelles"""
        print("=" * 60)
        print(f"    {GameConfig.MESSAGES['welcome']}")
        print("=" * 60)
        print(f"Score: {self.score} | Taux de réussite: {self.stats.get_win_rate():.1f}%")
        print(f"Parties: {self.stats.stats['games_won']}/{self.stats.stats['total_games']}")
        if self.stats.stats['best_score'] > 0:
            print(f"Meilleur score: {self.stats.stats['best_score']}")
        print("-" * 60)
    
    def choisir_difficulte(self) -> DifficultyLevel:
        """Permet au joueur de choisir la difficulté"""
        print("\n🎯 Choisissez votre niveau de difficulté:")
        for key, difficulty in GameConfig.DIFFICULTIES.items():
            print(f"{key}. {difficulty.name} (1-{difficulty.max_number}) - {difficulty.max_attempts} essais")
        
        while True:
            try:
                choix = input("\nVotre choix (1-4): ").strip()
                difficulty = GameConfig.get_difficulty(choix)
                self.current_difficulty = difficulty
                self.logger.info(f"Difficulté choisie: {difficulty.name}")
                return difficulty
            except ValueError as e:
                print(f"❌ {e}")
            except Exception as e:
                self.logger.error(f"Erreur lors du choix de difficulté: {e}")
                print(GameConfig.MESSAGES["invalid_choice"])
    
    def jouer_partie(self) -> bool:
        """Joue une partie de devinette"""
        try:
            difficulty = self.choisir_difficulte()
            self.secret_number = random.randint(1, difficulty.max_number)
            self.attempts = 0
            
            self.effacer_ecran()
            self.afficher_titre()
            print(f"\n🎯 Devinez un nombre entre 1 et {difficulty.max_number}")
            print(f"💡 Vous avez {difficulty.max_attempts} essais maximum")
            print("-" * 60)
            
            while self.attempts < difficulty.max_attempts:
                try:
                    self.attempts += 1
                    print(f"\nEssai {self.attempts}/{difficulty.max_attempts}")
                    proposition = int(input("Votre proposition: "))
                    
                    if proposition == self.secret_number:
                        return self._handle_win(difficulty)
                    else:
                        self._handle_wrong_guess(proposition)
                        
                except ValueError:
                    print(GameConfig.MESSAGES["invalid_input"])
                    self.attempts -= 1
            
            return self._handle_lose()
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la partie: {e}")
            print(f"❌ Une erreur est survenue: {e}")
            return False
    
    def _handle_win(self, difficulty: DifficultyLevel) -> bool:
        """Gère le cas où le joueur gagne"""
        points = GameConfig.calculate_points(self.attempts, difficulty.max_attempts)
        self.score += points
        
        print(f"\n{GameConfig.MESSAGES['win']} {self.secret_number}!")
        print(f"⭐ Points gagnés: {points}")
        print(f"🏆 Score total: {self.score}")
        
        self.stats.update_game(True, points, self.attempts, difficulty.name)
        self.logger.info(f"Partie gagnée - Score: {points}, Essais: {self.attempts}")
        
        return True
    
    def _handle_wrong_guess(self, proposition: int):
        """Gère une mauvaise proposition"""
        if proposition < self.secret_number:
            print(GameConfig.MESSAGES["higher"])
        else:
            print(GameConfig.MESSAGES["lower"])
        
        # Indicateur de proximité
        difference = abs(proposition - self.secret_number)
        proximity_msg = GameConfig.get_proximity_message(difference)
        print(proximity_msg)
    
    def _handle_lose(self) -> bool:
        """Gère le cas où le joueur perd"""
        print(f"\n{GameConfig.MESSAGES['lose']} {self.secret_number}")
        print(f"💔 Score actuel: {self.score}")
        
        if self.current_difficulty:
            self.stats.update_game(False, 0, self.attempts, self.current_difficulty.name)
        
        self.logger.info(f"Partie perdue - Essais: {self.attempts}")
        return False
    
    def afficher_stats(self):
        """Affiche les statistiques détaillées du joueur"""
        self.effacer_ecran()
        print("=" * 60)
        print("📊 STATISTIQUES DÉTAILLÉES")
        print("=" * 60)
        
        stats = self.stats.stats
        print(f"📈 Score total: {stats['total_score']}")
        print(f"🎮 Parties jouées: {stats['total_games']}")
        print(f"🏆 Parties gagnées: {stats['games_won']}")
        print(f"📊 Taux de réussite: {self.stats.get_win_rate():.1f}%")
        print(f"⭐ Meilleur score: {stats['best_score']}")
        print(f"🎯 Moyenne d'essais: {stats.get('average_attempts', 0):.1f}")
        
        if stats['last_played']:
            last_played = datetime.fromisoformat(stats['last_played'])
            print(f"🕐 Dernière partie: {last_played.strftime('%d/%m/%Y %H:%M')}")
        
        print("\n📈 Statistiques par difficulté:")
        for diff_name, diff_stats in stats['difficulty_stats'].items():
            win_rate = (diff_stats['wins'] / diff_stats['games'] * 100) if diff_stats['games'] > 0 else 0
            print(f"  • {diff_name}: {diff_stats['wins']}/{diff_stats['games']} ({win_rate:.1f}%)")
        
        print("=" * 60)
    
    def tutoriel(self):
        """Affiche le tutoriel du jeu"""
        self.effacer_ecran()
        print("=" * 60)
        print("🎓 TUTORIEL DU JEU")
        print("=" * 60)
        print("\n📋 COMMENT JOUER:")
        print("1. Choisissez un niveau de difficulté")
        print("2. Devinez le nombre secret")
        print("3. Utilisez les indices pour vous aider")
        print("4. Gagnez des points en trouvant rapidement!")
        print("\n🎯 INDICES:")
        print("📈 'C'est plus grand' - Votre nombre est trop petit")
        print("📉 'C'est plus petit' - Votre nombre est trop grand")
        print("🔥 'Très chaud' - Vous êtes très proche (≤5)")
        print("♨️ 'Chaud' - Vous êtes proche (≤10)")
        print("❄️ 'Tiède' - Vous êtes moyennement proche (≤20)")
        print("🧊 'Froid' - Vous êtes loin (>20)")
        print("\n⭐ POINTS:")
        print("• Points maximum: 100 (trouvé du 1er coup)")
        print("• Points minimum: 10")
        print("• Perte de 10 points par essai supplémentaire")
        print("\n💾 SAUVEGARDE:")
        print("• Vos statistiques sont sauvegardées automatiquement")
        print("• Vous pouvez suivre votre progression sur le long terme")
        print("=" * 60)
    
    def menu_principal(self):
        """Menu principal du jeu"""
        while True:
            self.effacer_ecran()
            self.afficher_titre()
            print("\n🎮 MENU PRINCIPAL")
            print("1. 🎯 Jouer une partie")
            print("2. 📊 Voir mes statistiques")
            print("3. 🎓 Mode tutoriel")
            print("4. 🚪 Quitter le jeu")
            
            try:
                choix = input("\nVotre choix (1-4): ").strip()
                
                if choix == "1":
                    self.jouer_partie()
                    input("\nAppuyez sur Entrée pour continuer...")
                elif choix == "2":
                    self.afficher_stats()
                    input("\nAppuyez sur Entrée pour continuer...")
                elif choix == "3":
                    self.tutoriel()
                    input("\nAppuyez sur Entrée pour continuer...")
                elif choix == "4":
                    print("\n👋 Merci d'avoir joué!")
                    print(f"🏆 Score final: {self.score}")
                    print(f"📊 Taux de réussite final: {self.stats.get_win_rate():.1f}%")
                    time.sleep(2)
                    break
                else:
                    print("❌ Choix invalide. Veuillez réessayer.")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print("\n\n👋 Au revoir!")
                break
            except Exception as e:
                self.logger.error(f"Erreur dans le menu principal: {e}")
                print("❌ Une erreur est survenue. Veuillez réessayer.")
                time.sleep(1)


def main():
    """Fonction principale du jeu"""
    try:
        jeu = JeuDevinette()
        jeu.menu_principal()
    except KeyboardInterrupt:
        print("\n\n👋 Au revoir!")
    except Exception as e:
        print(f"❌ Erreur critique: {e}")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
