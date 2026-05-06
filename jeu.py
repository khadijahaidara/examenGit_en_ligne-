<!--premiere ligne de jeu-->

import random
import time
import os

class JeuDevinette:
    """Jeu de devinette de nombre avec niveaux de difficulté"""
    
    def __init__(self):
        self.score = 0
        self.niveau = 1
        self.max_essais = 10
        self.parties_jouees = 0
        self.parties_gagnees = 0
        
    def effacer_ecran(self):
        """Efface l'écran de la console"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def afficher_titre(self):
        """Affiche le titre du jeu"""
        print("=" * 50)
        print("    🎮 JEU DE DEVINETTE DE NOMBRE 🎮")
        print("=" * 50)
        print(f"Score: {self.score} | Niveau: {self.niveau} | Parties gagnées: {self.parties_gagnees}/{self.parties_jouees}")
        print("-" * 50)
    
    def choisir_difficulte(self):
        """Permet au joueur de choisir la difficulté"""
        print("\nChoisissez votre niveau de difficulté:")
        print("1. Facile (1-50)")
        print("2. Moyen (1-100)")
        print("3. Difficile (1-200)")
        print("4. Expert (1-500)")
        
        while True:
            try:
                choix = int(input("Votre choix (1-4): "))
                if choix == 1:
                    return 50, 15
                elif choix == 2:
                    return 100, 10
                elif choix == 3:
                    return 200, 8
                elif choix == 4:
                    return 500, 6
                else:
                    print("Choix invalide. Veuillez réessayer.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    
    def jouer_partie(self):
        """Joue une partie de devinette"""
        self.parties_jouees += 1
        max_nombre, self.max_essais = self.choisir_difficulte()
        nombre_secret = random.randint(1, max_nombre)
        essais = 0
        
        self.effacer_ecran()
        self.afficher_titre()
        print(f"\n🎯 Devinez un nombre entre 1 et {max_nombre}")
        print(f"💡 Vous avez {self.max_essais} essais maximum")
        print("-" * 50)
        
        while essais < self.max_essais:
            try:
                essais += 1
                print(f"\nEssai {essais}/{self.max_essais}")
                proposition = int(input("Votre proposition: "))
                
                if proposition == nombre_secret:
                    self.parties_gagnees += 1
                    points = max(100 - (essais - 1) * 10, 10)
                    self.score += points
                    print(f"\n🎉 BRAVO! Vous avez trouvé le nombre {nombre_secret}!")
                    print(f"⭐ Points gagnés: {points}")
                    print(f"🏆 Score total: {self.score}")
                    return True
                elif proposition < nombre_secret:
                    print("📈 C'est plus grand!")
                else:
                    print("📉 C'est plus petit!")
                
                # Indicateur de proximité
                difference = abs(proposition - nombre_secret)
                if difference <= 5:
                    print("🔥 Très chaud!")
                elif difference <= 10:
                    print("♨️ Chaud!")
                elif difference <= 20:
                    print("❄️ Tiède!")
                else:
                    print("🧊 Froid!")
                    
            except ValueError:
                print("❌ Veuillez entrer un nombre valide.")
                essais -= 1
        
        print(f"\n😢 Dommage! Le nombre était {nombre_secret}")
        print(f"💔 Score actuel: {self.score}")
        return False
    
    def afficher_stats(self):
        """Affiche les statistiques du joueur"""
        print("\n" + "=" * 50)
        print("📊 STATISTIQUES DU JOUEUR")
        print("=" * 50)
        print(f"Score total: {self.score}")
        print(f"Parties jouées: {self.parties_jouees}")
        print(f"Parties gagnées: {self.parties_gagnees}")
        if self.parties_jouees > 0:
            taux_reussite = (self.parties_gagnees / self.parties_jouees) * 100
            print(f"Taux de réussite: {taux_reussite:.1f}%")
        print("=" * 50)
    
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
                choix = int(input("\nVotre choix (1-4): "))
                
                if choix == 1:
                    self.jouer_partie()
                    input("\nAppuyez sur Entrée pour continuer...")
                elif choix == 2:
                    self.afficher_stats()
                    input("\nAppuyez sur Entrée pour continuer...")
                elif choix == 3:
                    self.tutoriel()
                    input("\nAppuyez sur Entrée pour continuer...")
                elif choix == 4:
                    print("\n👋 Merci d'avoir joué!")
                    print(f"Score final: {self.score}")
                    time.sleep(2)
                    break
                else:
                    print("❌ Choix invalide. Veuillez réessayer.")
                    time.sleep(1)
                    
            except ValueError:
                print("❌ Veuillez entrer un nombre valide.")
                time.sleep(1)
    
    def tutoriel(self):
        """Affiche le tutoriel du jeu"""
        self.effacer_ecran()
        print("=" * 50)
        print("🎓 TUTORIEL DU JEU")
        print("=" * 50)
        print("\n📋 COMMENT JOUER:")
        print("1. Choisissez un niveau de difficulté")
        print("2. Devinez le nombre secret")
        print("3. Utilisez les indices pour vous aider")
        print("4. Gagnez des points en trouvant rapidement!")
        print("\n🎯 INDICES:")
        print("📈 'C'est plus grand' - Votre nombre est trop petit")
        print("📉 'C'est plus petit' - Votre nombre est trop grand")
        print("🔥 'Très chaud' - Vous êtes très proche!")
        print("♨️ 'Chaud' - Vous êtes proche")
        print("❄️ 'Tiède' - Vous êtes moyennement proche")
        print("🧊 'Froid' - Vous êtes loin")
        print("\n⭐ POINTS:")
        print("• Plus vous trouvez vite, plus vous gagnez de points")
        print("• Points minimum: 10")
        print("• Points maximum: 100")
        print("=" * 50)

def main():
    """Fonction principale du jeu"""
    jeu = JeuDevinette()
    jeu.menu_principal()

if __name__ == "__main__":
    main()
