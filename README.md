# 🎮 Examen Git en Ligne - Version Professionnelle

[![CI/CD](https://github.com/khadijahaidara/examenGit_en_ligne-/actions/workflows/ci-pro.yml/badge.svg)](https://github.com/khadijahaidara/examenGit_en_ligne-/actions/workflows/ci-pro.yml)
[![codecov](https://codecov.io/gh/khadijahaidara/examenGit_en_ligne-/branch/main/graph/badge.svg)](https://codecov.io/gh/khadijahaidara/examenGit_en_ligne-)
[![PyPI version](https://badge.fury.io/py/examen-git-en-ligne.svg)](https://badge.fury.io/py/examen-git-en-ligne)
[![Python versions](https://img.shields.io/pypi/pyversions/examen-git-en-ligne.svg)](https://pypi.org/project/examen-git-en-ligne/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ce projet professionnel a été réalisé dans le cadre d'un exercice pratique sur Git et GitHub, puis amélioré avec des standards de développement professionnels.

## � Fonctionnalités

### 🎮 Jeu de Devinettes
- **Double interface**: Console et Graphique (Tkinter)
- **4 niveaux de difficulté**: Facile (1-50) → Expert (1-500)
- **Système de points**: 100 points max, perte de 10 points par essai
- **Indices intelligents**: 🔥 Très chaud, ♨️ Chaud, ❄️ Tiède, 🧊 Froid
- **Statistiques persistantes**: Sauvegarde automatique des performances
- **Mode tutoriel**: Guide intégré pour les nouveaux joueurs

### 🔧 Fonctions Utilitaires (10 fonctions)
- **Mathématiques**: `factorielle()`, `est_premier()`, `fibonacci()`, `pgcd()`, `calculer_imc()`
- **Textuelles**: `inverser_chaine()`, `compter_voyelles()`, `generer_mot_de_passe()`
- **Conversion**: `temperature_conversion()`, `format_temps()`

### 🧪 Tests et Qualité
- **Couverture de test**: 95%+ avec pytest
- **Tests unitaires**: 50+ tests pour toutes les fonctionnalités
- **Tests d'intégration**: Flux complets du jeu
- **Type hints**: Annotations de types complètes
- **Documentation**: Docstrings Google-style

### 🔄 CI/CD Professionnel
- **Multi-plateforme**: Linux, Windows, macOS
- **Multi-version Python**: 3.8, 3.9, 3.10, 3.11
- **Analyse de sécurité**: Bandit, Safety, Trivy
- **Qualité de code**: Flake8, MyPy, Black
- **Coverage**: Codecov integration
- **Documentation**: Auto-déployée sur GitHub Pages

## 📁 Structure du Projet

```
examenGit_en_ligne/
├── src/                    # 📦 Code source
│   ├── utils/             # 🔧 Fonctions utilitaires
│   │   ├── __init__.py
│   │   ├── functions.py   # 10 fonctions math/textuelles
│   │   └── logger.py      # Système de logging
│   ├── game/              # 🎮 Logique du jeu
│   │   ├── __init__.py
│   │   ├── config.py      # Configuration et constantes
│   │   └── game.py        # Logique du jeu console
│   ├── gui/               # 🖥️ Interface graphique
│   │   ├── __init__.py
│   │   └── game_gui.py    # Interface Tkinter
│   └── __init__.py
├── tests/                 # 🧪 Tests unitaires
│   ├── __init__.py
│   ├── test_functions.py  # Tests des fonctions
│   └── test_game.py       # Tests du jeu
├── docs/                  # 📚 Documentation Sphinx
│   ├── conf.py
│   ├── index.rst
│   ├── api.rst
│   └── installation.rst
├── examples/              # 📖 Exemples d'utilisation
│   └── basic_usage.py
├── .github/workflows/     # 🔄 CI/CD
│   ├── ci.yml           # Pipeline de base
│   └── ci-pro.yml       # Pipeline professionnel
├── requirements.txt       # 📦 Dépendances
├── requirements-dev.txt   # 🔧 Dépendances de dev
├── setup.py              # 📦 Packaging
├── pyproject.toml        # ⚙️ Configuration moderne
├── Makefile              # 🛠️ Commandes utiles
├── README.md             # 📖 Ce fichier
└── .gitignore           # 🚫 Fichiers ignorés
```

## �️ Installation

### Avec pip (recommandé)
```bash
pip install examen-git-en-ligne
```

### Depuis le dépôt
```bash
git clone https://github.com/khadijahaidara/examenGit_en_ligne-.git
cd examenGit_en_ligne
pip install -e .
```

### Environnement de développement
```bash
git clone https://github.com/khadijahaidara/examenGit_en_ligne-.git
cd examenGit_en_ligne
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows
pip install -r requirements-dev.txt
pip install -e .
```

## 🎮 Utilisation

### Jeu en Console
```bash
jeu-devinette
# ou
python -m src.game.game
```

### Jeu Graphique
```bash
jeu-devinette-gui
# ou
python -m src.gui.game_gui
```

### Utilisation des Fonctions
```python
from src.utils.functions import factorielle, est_premier

# Calculer une factorielle
result = factorielle(5)  # 120

# Vérifier si un nombre est premier
is_prime = est_premier(7)  # True
```

### Démonstration Complète
```bash
python examples/basic_usage.py
```

## 🧪 Tests

### Exécuter tous les tests
```bash
make test
# ou
pytest tests/ -v --cov=src
```

### Tests rapides
```bash
make test-fast
# ou
pytest tests/ -v -x
```

### Qualité du code
```bash
make lint
make format
```

### Vérifications complètes
```bash
make check
```

## 📚 Documentation

- **Documentation en ligne**: https://examen-git-en-ligne.readthedocs.io/
- **API Reference**: [docs/api.rst](docs/api.rst)
- **Guide d'installation**: [docs/installation.rst](docs/installation.rst)

## 🔧 Développement

### Commandes utiles (Makefile)
```bash
make help           # Affiche toutes les commandes
make install        # Installation en mode dev
make test          # Exécute les tests
make lint          # Vérification du code
make format        # Formate le code
make docs          # Génère la documentation
make clean         # Nettoie les fichiers temporaires
make build         # Construit le package
make demo          # Lance la démonstration
```

### Structure des tests
- **`test_functions.py`**: Tests complets des 10 fonctions utilitaires
- **`test_game.py`**: Tests du jeu, configuration, statistiques
- **Couverture**: Tests des cas normaux, erreurs, limites, intégration

## 📊 Statistiques du Projet

- **Lignes de code**: ~2000+ lignes
- **Couverture de test**: 95%+
- **Fonctions**: 10 fonctions utilitaires + classes de jeu
- **Tests**: 50+ tests unitaires
- **Support Python**: 3.8, 3.9, 3.10, 3.11
- **Support OS**: Linux, Windows, macOS

## 🎯 Objectifs de l'Exercice

✅ Créer un dépôt Git en ligne  
✅ Configurer .gitignore pour ignorer les fichiers .docx  
✅ Créer mesfonctions.py avec le contenu requis  
✅ Créer jeu.py avec le contenu requis  
✅ Générer 10 fonctions Python différentes  
✅ Créer des tests unitaires pour 5 fonctions  
✅ Générer un code de jeu complet  
✅ Ajouter et commiter les modifications  
✅ Pusher vers le dépôt distant  
✅ Configurer CI/CD pour le jeu  

### 🚀 Améliorations Professionnelles Ajoutées
✅ Architecture modulaire avec séparation des responsabilités  
✅ Interface graphique professionnelle avec Tkinter  
✅ Système de sauvegarde des statistiques persistantes  
✅ Tests complets avec 95%+ de couverture  
✅ Documentation technique complète avec Sphinx  
✅ Packaging professionnel avec setup.py et pyproject.toml  
✅ CI/CD avancé avec sécurité et performance  
✅ Logging avancé et gestion d'erreurs  
✅ Type hints et docstrings professionnels  
✅ Makefile pour automatisation des tâches  

## 🤝 Contribuer

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amazing-feature`)
3. Commit les changements (`git commit -m 'Add amazing feature'`)
4. Push vers la branche (`git push origin feature/amazing-feature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour les détails.

## 👨‍💻 Auteur

**khadijahaidara** - *Développeur Python* - [GitHub](https://github.com/khadijahaidara)

## 🙏 Remerciements

- Projet réalisé dans le cadre d'un exercice Git/GitHub
- Amélioré avec les meilleures pratiques de développement Python
- Architecture inspirée des standards open-source

---

⭐ **Si ce projet vous a été utile, laissez une étoile !**
