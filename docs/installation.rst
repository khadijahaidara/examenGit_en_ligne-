Installation
============

Prérequis
---------

* Python 3.8 ou supérieur
* pip (gestionnaire de paquets Python)
* Git (pour cloner le dépôt)

Installation depuis le dépôt
----------------------------

1. Cloner le dépôt:

.. code-block:: bash

   git clone https://github.com/khadijahaidara/examenGit_en_ligne-.git
   cd examenGit_en_ligne

2. Créer un environnement virtuel (recommandé):

.. code-block:: bash

   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate

3. Installer les dépendances:

.. code-block:: bash

   pip install -r requirements.txt

4. Installer le package en mode développement:

.. code-block:: bash

   pip install -e .

Dépendances
-----------

Le projet nécessite les dépendances suivantes:

* **pytest**: Pour exécuter les tests
* **sphinx**: Pour générer la documentation
* **sphinx-rtd-theme**: Thème pour la documentation
* **tkinter**: Pour l'interface graphique (généralement inclus avec Python)

Installation des dépendances de développement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour installer les dépendances de développement supplémentaires:

.. code-block:: bash

   pip install -r requirements-dev.txt

Vérification de l'installation
------------------------------

Pour vérifier que l'installation s'est bien déroulée:

1. Tester l'importation des modules:

.. code-block:: python

   from src.utils.functions import factorielle
   from src.game.game import JeuDevinette
   print("Installation réussie!")

2. Exécuter les tests:

.. code-block:: bash

   python -m pytest tests/ -v

3. Lancer le jeu:

.. code-block:: bash

   # Version console
   python -m src.game.game
   
   # Version graphique
   python -m src.gui.game_gui

Configuration
-------------

Variables d'environnement
~~~~~~~~~~~~~~~~~~~~~~~~~

Le projet utilise les variables d'environnement suivantes (optionnelles):

* ``GAME_STATS_FILE``: Chemin du fichier de sauvegarde des statistiques
* ``GAME_LOG_LEVEL``: Niveau de logging (DEBUG, INFO, WARNING, ERROR)
* ``GAME_LOG_FILE``: Chemin du fichier de log

Exemple:

.. code-block:: bash

   export GAME_STATS_FILE="/path/to/custom_stats.json"
   export GAME_LOG_LEVEL="DEBUG"

Fichiers de configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

* **.gitignore**: Fichiers ignorés par Git
* **game_stats.json**: Sauvegarde des statistiques (créé automatiquement)
* **logs/**: Dossiers des logs (créé automatiquement)

Dépannage
----------

Problèmes courants
~~~~~~~~~~~~~~~~~

**ImportError: No module named 'src'**

Solution: Assurez-vous d'être dans le répertoire racine du projet ou d'installer le package avec ``pip install -e .``

**Tkinter non disponible**

Solution: Sur certaines distributions Linux, Tkinter doit être installé séparément:

.. code-block:: bash

   # Ubuntu/Debian
   sudo apt-get install python3-tk
   
   # Fedora
   sudo dnf install python3-tkinter

**Tests qui échouent**

Solution: Vérifiez que toutes les dépendances sont installées et que vous utilisez une version compatible de Python (3.8+).

Support
-------

En cas de problème:

1. Vérifiez les `logs <https://github.com/khadijahaidara/examenGit_en_ligne-/tree/main/logs>`_ pour des messages d'erreur détaillés
2. Consultez les `issues <https://github.com/khadijahaidara/examenGit_en_ligne-/issues>`_ sur GitHub
3. Créez une nouvelle issue avec les détails du problème
