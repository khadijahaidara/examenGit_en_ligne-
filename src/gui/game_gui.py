"""
Interface graphique Tkinter pour le jeu de devinette
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
from typing import Optional
from ..game.config import GameConfig, DifficultyLevel
from ..game.game import GameStats


class GameGUI:
    """Interface graphique pour le jeu de devinette"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎮 Jeu de Devinettes")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Configuration du style
        self.setup_styles()
        
        # Variables du jeu
        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 10
        self.current_difficulty: Optional[DifficultyLevel] = None
        self.game_active = False
        
        # Statistiques
        self.stats = GameStats("gui_game_stats.json")
        
        # Création de l'interface
        self.create_widgets()
        
        # Configuration des couleurs
        self.setup_colors()
    
    def setup_styles(self):
        """Configure les styles ttk"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configuration des styles personnalisés
        self.style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        self.style.configure('Subtitle.TLabel', font=('Arial', 12))
        self.style.configure('Success.TLabel', font=('Arial', 10), foreground='green')
        self.style.configure('Error.TLabel', font=('Arial', 10), foreground='red')
        self.style.configure('Game.TButton', font=('Arial', 10, 'bold'))
    
    def setup_colors(self):
        """Configure les couleurs de l'application"""
        self.colors = {
            'bg': '#f0f0f0',
            'fg': '#333333',
            'button': '#4CAF50',
            'button_hover': '#45a049',
            'success': '#4CAF50',
            'error': '#f44336',
            'warning': '#ff9800',
            'info': '#2196F3'
        }
        
        self.root.configure(bg=self.colors['bg'])
    
    def create_widgets(self):
        """Crée tous les widgets de l'interface"""
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Titre
        self.create_title()
        
        # Frame de jeu
        self.create_game_frame()
        
        # Frame de contrôle
        self.create_control_frame()
        
        # Frame de statistiques
        self.create_stats_frame()
        
        # Frame d'historique
        self.create_history_frame()
    
    def create_title(self):
        """Crée le titre du jeu"""
        title_frame = ttk.Frame(self.main_frame)
        title_frame.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        title_label = ttk.Label(
            title_frame, 
            text="🎮 JEU DE DEVINETTES", 
            style='Title.TLabel'
        )
        title_label.pack()
        
        self.subtitle_label = ttk.Label(
            title_frame,
            text="Choisissez une difficulté pour commencer",
            style='Subtitle.TLabel'
        )
        self.subtitle_label.pack()
    
    def create_game_frame(self):
        """Crée la frame de jeu principale"""
        self.game_frame = ttk.LabelFrame(self.main_frame, text="🎯 Jeu", padding="15")
        self.game_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Information de partie
        self.game_info_label = ttk.Label(self.game_frame, text="Partie non démarrée")
        self.game_info_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Champ de saisie
        ttk.Label(self.game_frame, text="Votre proposition:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.guess_entry = ttk.Entry(self.game_frame, font=('Arial', 12), width=15)
        self.guess_entry.grid(row=1, column=1, pady=5)
        self.guess_entry.bind('<Return>', lambda e: self.make_guess())
        
        # Bouton de proposition
        self.guess_button = ttk.Button(
            self.game_frame, 
            text="Deviner", 
            command=self.make_guess,
            style='Game.TButton'
        )
        self.guess_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Label de résultat
        self.result_label = ttk.Label(self.game_frame, text="", style='Subtitle.TLabel')
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)
        
        # Label de proximité
        self.proximity_label = ttk.Label(self.game_frame, text="", style='Subtitle.TLabel')
        self.proximity_label.grid(row=4, column=0, columnspan=2, pady=5)
    
    def create_control_frame(self):
        """Crée la frame de contrôle"""
        self.control_frame = ttk.LabelFrame(self.main_frame, text="🎮 Contrôles", padding="15")
        self.control_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N), pady=(0, 10))
        
        # Difficultés
        difficulties_frame = ttk.Frame(self.control_frame)
        difficulties_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(difficulties_frame, text="Difficulté:").pack(side=tk.LEFT, padx=(0, 10))
        
        self.difficulty_var = tk.StringVar(value="1")
        for i, (key, diff) in enumerate(GameConfig.DIFFICULTIES.items()):
            rb = ttk.Radiobutton(
                difficulties_frame, 
                text=f"{diff.name} (1-{diff.max_number})", 
                variable=self.difficulty_var, 
                value=key,
                command=self.on_difficulty_change
            )
            rb.pack(side=tk.LEFT, padx=5)
        
        # Boutons de contrôle
        buttons_frame = ttk.Frame(self.control_frame)
        buttons_frame.pack(fill=tk.X)
        
        self.new_game_button = ttk.Button(
            buttons_frame, 
            text="🆕 Nouvelle Partie", 
            command=self.new_game,
            style='Game.TButton'
        )
        self.new_game_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.reset_stats_button = ttk.Button(
            buttons_frame, 
            text="🔄 Réinitialiser Stats", 
            command=self.reset_stats
        )
        self.reset_stats_button.pack(side=tk.LEFT)
    
    def create_stats_frame(self):
        """Crée la frame des statistiques"""
        self.stats_frame = ttk.LabelFrame(self.main_frame, text="📊 Statistiques", padding="15")
        self.stats_frame.grid(row=2, column=1, sticky=(tk.W, tk.E, tk.N), pady=(0, 10), padx=(10, 0))
        
        self.stats_text = tk.Text(self.stats_frame, width=30, height=8, font=('Courier', 9))
        self.stats_text.pack()
        self.stats_text.config(state=tk.DISABLED)
        
        self.update_stats_display()
    
    def create_history_frame(self):
        """Crée la frame d'historique des propositions"""
        self.history_frame = ttk.LabelFrame(self.main_frame, text="📜 Historique", padding="15")
        self.history_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        
        self.history_text = scrolledtext.ScrolledText(
            self.history_frame, 
            width=70, 
            height=8, 
            font=('Courier', 9),
            state=tk.DISABLED
        )
        self.history_text.pack(fill=tk.BOTH, expand=True)
    
    def on_difficulty_change(self):
        """Gère le changement de difficulté"""
        if self.game_active:
            if messagebox.askyesno("Changement de difficulté", 
                                "Voulez-vous redémarrer la partie avec la nouvelle difficulté ?"):
                self.new_game()
            else:
                # Restaurer la difficulté précédente
                if self.current_difficulty:
                    for key, diff in GameConfig.DIFFICULTIES.items():
                        if diff.name == self.current_difficulty.name:
                            self.difficulty_var.set(key)
                            break
    
    def new_game(self):
        """Démarre une nouvelle partie"""
        try:
            # Récupérer la difficulté choisie
            difficulty = GameConfig.get_difficulty(self.difficulty_var.get())
            self.current_difficulty = difficulty
            self.max_attempts = difficulty.max_attempts
            
            # Générer le nombre secret
            self.secret_number = random.randint(1, difficulty.max_number)
            self.attempts = 0
            self.game_active = True
            
            # Mettre à jour l'interface
            self.game_info_label.config(
                text=f"Devinez un nombre entre 1 et {difficulty.max_number} ({difficulty.max_attempts} essais max)"
            )
            self.result_label.config(text="")
            self.proximity_label.config(text="")
            self.guess_entry.delete(0, tk.END)
            self.guess_entry.config(state=tk.NORMAL)
            self.guess_button.config(state=tk.NORMAL)
            
            # Vider l'historique
            self.history_text.config(state=tk.NORMAL)
            self.history_text.delete(1.0, tk.END)
            self.history_text.config(state=tk.DISABLED)
            
            # Mettre le focus sur le champ de saisie
            self.guess_entry.focus()
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du démarrage de la partie: {e}")
    
    def make_guess(self):
        """Fait une proposition"""
        if not self.game_active:
            messagebox.showwarning("Partie non démarrée", "Veuillez démarrer une nouvelle partie")
            return
        
        try:
            guess_text = self.guess_entry.get().strip()
            if not guess_text:
                return
            
            guess = int(guess_text)
            self.guess_entry.delete(0, tk.END)
            
            self.attempts += 1
            
            # Ajouter à l'historique
            self.add_to_history(f"Essai {self.attempts}: {guess}")
            
            if guess == self.secret_number:
                self.handle_win()
            elif self.attempts >= self.max_attempts:
                self.handle_lose()
            else:
                self.handle_wrong_guess(guess)
                
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide")
    
    def handle_win(self):
        """Gère une victoire"""
        self.game_active = False
        
        points = GameConfig.calculate_points(self.attempts, self.max_attempts)
        
        # Mettre à jour les statistiques
        self.stats.update_game(True, points, self.attempts, self.current_difficulty.name)
        self.update_stats_display()
        
        # Afficher le résultat
        self.result_label.config(
            text=f"🎉 BRAVO! Nombre trouvé: {self.secret_number}",
            style='Success.TLabel'
        )
        self.proximity_label.config(
            text=f"⭐ Points gagnés: {points} | Essais: {self.attempts}/{self.max_attempts}",
            style='Success.TLabel'
        )
        
        # Désactiver les contrôles
        self.guess_entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)
        
        # Message de félicitations
        messagebox.showinfo("Victoire!", 
                          f"Félicitations! Vous avez trouvé le nombre {self.secret_number}!\n"
                          f"Points gagnés: {points}\n"
                          f"Essais utilisés: {self.attempts}/{self.max_attempts}")
    
    def handle_lose(self):
        """Gère une défaite"""
        self.game_active = False
        
        # Mettre à jour les statistiques
        self.stats.update_game(False, 0, self.attempts, self.current_difficulty.name)
        self.update_stats_display()
        
        # Afficher le résultat
        self.result_label.config(
            text=f"😢 Dommage! Le nombre était: {self.secret_number}",
            style='Error.TLabel'
        )
        self.proximity_label.config(
            text=f"Essais utilisés: {self.attempts}/{self.max_attempts}",
            style='Error.TLabel'
        )
        
        # Désactiver les contrôles
        self.guess_entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)
        
        # Message de défaite
        messagebox.showinfo("Partie terminée", 
                          f"Dommage! Le nombre était {self.secret_number}.\n"
                          f"Essayez encore!")
    
    def handle_wrong_guess(self, guess):
        """Gère une mauvaise proposition"""
        if guess < self.secret_number:
            direction = "plus grand"
            emoji = "📈"
        else:
            direction = "plus petit"
            emoji = "📉"
        
        self.result_label.config(text=f"{emoji} C'est {direction}!")
        
        # Indicateur de proximité
        difference = abs(guess - self.secret_number)
        proximity_msg = GameConfig.get_proximity_message(difference)
        self.proximity_label.config(text=f"{proximity_msg} | Essais: {self.attempts}/{self.max_attempts}")
        
        # Changer la couleur selon la proximité
        if difference <= 5:
            self.proximity_label.config(style='Success.TLabel')
        elif difference <= 10:
            self.proximity_label.config(style='Subtitle.TLabel')
        else:
            self.proximity_label.config(style='Error.TLabel')
    
    def add_to_history(self, message):
        """Ajoute un message à l'historique"""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.insert(tk.END, message + "\n")
        self.history_text.see(tk.END)
        self.history_text.config(state=tk.DISABLED)
    
    def update_stats_display(self):
        """Met à jour l'affichage des statistiques"""
        stats = self.stats.stats
        
        stats_text = f"""Parties jouées: {stats['total_games']}
Parties gagnées: {stats['games_won']}
Taux de réussite: {self.stats.get_win_rate():.1f}%
Score total: {stats['total_score']}
Meilleur score: {stats['best_score']}
Moyenne essais: {stats.get('average_attempts', 0):.1f}"""
        
        self.stats_text.config(state=tk.NORMAL)
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.insert(1.0, stats_text)
        self.stats_text.config(state=tk.DISABLED)
    
    def reset_stats(self):
        """Réinitialise les statistiques"""
        if messagebox.askyesno("Réinitialiser", 
                                "Voulez-vous vraiment réinitialiser toutes les statistiques ?"):
            self.stats = GameStats("gui_game_stats.json")
            self.update_stats_display()
            messagebox.showinfo("Statistiques", "Les statistiques ont été réinitialisées")
    
    def run(self):
        """Démarre l'interface graphique"""
        self.root.mainloop()


def main():
    """Fonction principale pour l'interface graphique"""
    try:
        app = GameGUI()
        app.run()
    except Exception as e:
        messagebox.showerror("Erreur critique", f"Une erreur critique est survenue: {e}")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
