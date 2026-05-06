API Reference
=============

Ce document décrit l'API complète du projet examenGit_en_ligne.

Modules utils
-------------

.. automodule:: src.utils.functions
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: src.utils.logger
   :members:
   :undoc-members:
   :show-inheritance:

Modules game
-----------

.. automodule:: src.game.config
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: src.game.game
   :members:
   :undoc-members:
   :show-inheritance:

Modules GUI
-----------

.. automodule:: src.gui.game_gui
   :members:
   :undoc-members:
   :show-inheritance:

Classes principales
------------------

GameStats
~~~~~~~~~

.. autoclass:: src.game.game.GameStats
   :members:
   :undoc-members:
   :show-inheritance:

JeuDevinette
~~~~~~~~~~~

.. autoclass:: src.game.game.JeuDevinette
   :members:
   :undoc-members:
   :show-inheritance:

GameGUI
~~~~~~~

.. autoclass:: src.gui.game_gui.GameGUI
   :members:
   :undoc-members:
   :show-inheritance:

GameConfig
~~~~~~~~~~

.. autoclass:: src.game.config.GameConfig
   :members:
   :undoc-members:
   :show-inheritance:

DifficultyLevel
~~~~~~~~~~~~~~

.. autoclass:: src.game.config.DifficultyLevel
   :members:
   :undoc-members:
   :show-inheritance:

Fonctions utilitaires
--------------------

Mathématiques
~~~~~~~~~~~~~

.. autofunction:: src.utils.functions.factorielle
.. autofunction:: src.utils.functions.est_premier
.. autofunction:: src.utils.functions.fibonacci
.. autofunction:: src.utils.functions.pgcd
.. autofunction:: src.utils.functions.calculer_imc

Textuelles
~~~~~~~~~~

.. autofunction:: src.utils.functions.inverser_chaine
.. autofunction:: src.utils.functions.compter_voyelles
.. autofunction:: src.utils.functions.generer_mot_de_passe

Conversion
~~~~~~~~~~

.. autofunction:: src.utils.functions.temperature_conversion
.. autofunction:: src.utils.functions.format_temps

Exceptions
---------

Le projet peut lever les exceptions suivantes:

.. autoexception:: ValueError
   :show-inheritance:

Exemples d'utilisation
--------------------

Utilisation des fonctions
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from src.utils.functions import factorielle, est_premier
   
   # Calculer une factorielle
   result = factorielle(5)  # Returns: 120
   
   # Vérifier si un nombre est premier
   is_prime = est_premier(7)  # Returns: True

Utilisation du jeu en console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from src.game.game import JeuDevinette
   
   # Créer une instance du jeu
   game = JeuDevinette()
   
   # Lancer le menu principal
   game.menu_principal()

Utilisation de l'interface graphique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from src.gui.game_gui import GameGUI
   
   # Créer et lancer l'interface graphique
   app = GameGUI()
   app.run()

Gestion des statistiques
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from src.game.game import GameStats
   
   # Créer une instance de gestionnaire de statistiques
   stats = GameStats("custom_stats.json")
   
   # Mettre à jour après une partie
   stats.update_game(won=True, score=100, attempts=3, difficulty="Moyen")
   
   # Obtenir le taux de réussite
   win_rate = stats.get_win_rate()
