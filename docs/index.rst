Bienvenue dans la documentation de examenGit_en_ligne!
==========================================================

Ce projet a été réalisé dans le cadre d'un exercice pratique sur Git et GitHub.
Il comprend un jeu de devinette de nombre, des fonctions utilitaires et des tests complets.

.. toctree::
   :maxdepth: 2
   :caption: Contenu:

   installation
   api
   examples
   contributing

Fonctionnalités
--------------

* 🎮 **Jeu de devinette**: Interface console et graphique avec 4 niveaux de difficulté
* 🔧 **Fonctions utilitaires**: 10 fonctions mathématiques et textuelles
* 🧪 **Tests complets**: Couverture de test élevée avec unittest
* 📊 **Statistiques**: Sauvegarde automatique des performances
* 🔄 **CI/CD**: Pipeline GitHub Actions automatisé
* 📚 **Documentation**: Documentation technique complète

Structure du projet
-------------------

::

    examenGit_en_ligne/
    ├── src/                    # Code source
    │   ├── utils/             # Fonctions utilitaires
    │   ├── game/              # Logique du jeu
    │   └── gui/               # Interface graphique
    ├── tests/                 # Tests unitaires
    ├── docs/                  # Documentation
    └── .github/workflows/    # CI/CD

Démarrage rapide
---------------

Installation
~~~~~~~~~~~~~

.. code-block:: bash

   pip install -e .

Lancer le jeu en console
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python -m src.game.game

Lancer le jeu graphique
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python -m src.gui.game_gui

Exécuter les tests
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python -m pytest tests/

Indices et recherche
===================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
