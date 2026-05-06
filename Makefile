# Makefile pour le projet examenGit_en_ligne

.PHONY: help install install-dev test lint format clean docs build upload demo run-game run-gui

# Variables
PYTHON := python3
PIP := pip3
PYTEST := pytest
BLACK := black
FLAKE8 := flake8
MYPY := mypy
BANDIT := bandit

# Cible par défaut
help:
	@echo "Commandes disponibles:"
	@echo "  install      - Installer le package en mode développement"
	@echo "  install-dev  - Installer les dépendances de développement"
	@echo "  test         - Exécuter les tests"
	@echo "  lint         - Vérifier le code avec flake8 et mypy"
	@echo "  format       - Formater le code avec black et isort"
	@echo "  clean        - Nettoyer les fichiers temporaires"
	@echo "  docs         - Générer la documentation"
	@echo "  build        - Construire le package"
	@echo "  upload       - Uploader vers PyPI"
	@echo "  demo         - Lancer la démonstration"
	@echo "  run-game     - Lancer le jeu en console"
	@echo "  run-gui      - Lancer le jeu graphique"

# Installation
install:
	$(PIP) install -e .

install-dev:
	$(PIP) install -r requirements-dev.txt
	$(PIP) install -e .

# Tests
test:
	$(PYTEST) tests/ -v --cov=src --cov-report=html --cov-report=term-missing

test-fast:
	$(PYTEST) tests/ -v -x

# Qualité du code
lint:
	$(FLAKE8) src/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics
	$(FLAKE8) src/ tests/ --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
	$(MYPY) src/ --ignore-missing-imports --no-strict-optional || true
	$(BANDIT) -r src/ -f json -o bandit-report.json || true

format:
	$(BLACK) src/ tests/ examples/
	isort src/ tests/ examples/

# Nettoyage
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# Documentation
docs:
	cd docs && make html

docs-live:
	cd docs && make livehtml

# Build et distribution
build: clean
	$(PYTHON) -m build

upload: build
	$(PYTHON) -m twine upload dist/*

upload-test: build
	$(PYTHON) -m twine upload --repository testpypi dist/*

# Démonstration
demo:
	$(PYTHON) examples/basic_usage.py

# Lancement du jeu
run-game:
	$(PYTHON) -m src.game.game

run-gui:
	$(PYTHON) -m src.gui.game_gui

# Vérifications complètes
check: format lint test
	@echo "✅ Toutes les vérifications complétées"

# Pré-commit
pre-commit: format lint test
	@echo "✅ Pré-commit complété"

# Installation des outils de développement
setup-dev:
	$(PIP) install pre-commit
	pre-commit install

# Analyse de sécurité
security:
	$(BANDIT) -r src/
	safety check

# Performance
profile:
	$(PYTHON) -m cProfile -o profile.stats -m src.game.game
	$(PYTHON) -c "
import pstats
p = pstats.Stats('profile.stats')
p.sort_stats('cumulative')
p.print_stats(20)
"

# Dépendances
deps:
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt

# Mise à jour des dépendances
update-deps:
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade -r requirements.txt
	$(PIP) install --upgrade -r requirements-dev.txt

# Vérification de la version
version:
	@$(PYTHON) -c "import src; print(f'Version: {src.__version__}')"

# Informations sur le projet
info:
	@echo "Projet: examenGit_en_ligne"
	@echo "Version: $(shell $(PYTHON) -c 'import src; print(src.__version__)')"
	@echo "Python: $(shell $(PYTHON) --version)"
	@echo "Pip: $(shell $(PIP) --version)"
