# Examen Git en Ligne

Ce projet a été réalisé dans le cadre d'un exercice pratique sur Git et GitHub.

## 📋 Contenu du projet

### 📁 Fichiers principaux

- **`mesfonctions.py`** - Contient 10 fonctions Python différentes
  - `factorielle(n)` - Calcule la factorielle d'un nombre
  - `est_premier(nombre)` - Vérifie si un nombre est premier
  - `generer_mot_de_passe(longueur=12)` - Génère un mot de passe sécurisé
  - `fibonacci(n)` - Génère la suite de Fibonacci
  - `calculer_imc(poids, taille)` - Calcule l'IMC
  - `inverser_chaine(chaine)` - Inverse une chaîne de caractères
  - `compter_voyelles(texte)` - Compte les voyelles dans un texte
  - `temperature_conversion(celsius, vers_fahrenheit=True)` - Convertit les températures
  - `pgcd(a, b)` - Calcule le PGCD
  - `format_temps(secondes)` - Convertit les secondes en format HH:MM:SS

- **`jeu.py`** - Jeu de devinette de nombre complet avec:
  - Menu principal interactif
  - 4 niveaux de difficulté
  - Système de score
  - Statistiques du joueur
  - Mode tutoriel
  - Indices de proximité (chaud/froid)

- **`test_mesfonctions.py`** - Tests unitaires pour 5 fonctions
  - Tests pour `factorielle`, `est_premier`, `fibonacci`, `calculer_imc`, `inverser_chaine`

- **`.gitignore`** - Configure Git pour ignorer les fichiers `.docx` et autres fichiers temporaires

### 🔄 CI/CD

Le projet inclut un pipeline GitHub Actions (`.github/workflows/ci.yml`) qui:
- Teste les fonctions sur Python 3.8, 3.9, 3.10, 3.11
- Exécute les tests unitaires avec pytest
- Vérifie l'importation des modules
- Effectue le linting avec flake8
- Teste la classe du jeu

## 🚀 Comment utiliser

### Pour tester les fonctions:
```bash
python test_mesfonctions.py
```

### Pour jouer au jeu:
```bash
python jeu.py
```

### Pour tester individuellement les fonctions:
```python
import mesfonctions
print(mesfonctions.factorielle(5))  # 120
print(mesfonctions.est_premier(7))  # True
```

## 📦 Instructions pour finaliser le dépôt

1. **Créez le dépôt sur GitHub:**
   - Allez sur https://github.com/khadijahaidara
   - Cliquez sur "New repository"
   - Nom: `examenGit_en_ligne`
   - Public ou Private (votre choix)
   - NE cochez PAS "Add a README file" (nous en avons déjà un)
   - Cliquez sur "Create repository"

2. **Poussez le code:**
   ```bash
   git push -u origin master
   ```

3. **Vérifiez le CI/CD:**
   - Allez dans l'onglet "Actions" de votre dépôt
   - Vous devriez voir le pipeline s'exécuter automatiquement

## 🎯 Objectifs de l'exercice

✅ Créer un dépôt Git en ligne  
✅ Configurer .gitignore pour ignorer les fichiers .docx  
✅ Créer mesfonctions.py avec le contenu requis  
✅ Créer jeu.py avec le contenu requis  
✅ Générer 10 fonctions Python différentes  
✅ Créer des tests unitaires pour 5 fonctions  
✅ Générer un code de jeu complet  
✅ Ajouter et commiter les modifications  
⏳ Pusher vers le dépôt distant (nécessite création du dépôt GitHub)  
✅ Configurer CI/CD pour le jeu  

## 🎮 Jeu de Devinette

Le jeu inclut:
- **4 niveaux de difficulté**: Facile (1-50), Moyen (1-100), Difficile (1-200), Expert (1-500)
- **Système de score**: Plus vous trouvez vite, plus vous gagnez de points
- **Indices visuels**: 🔥 Très chaud, ♨️ Chaud, ❄️ Tiède, 🧊 Froid
- **Statistiques**: Suivi des parties jouées et gagnées
- **Mode tutoriel**: Instructions détaillées pour les nouveaux joueurs

---

**Auteur:** khadijahaidara  
**Date:** 2026
