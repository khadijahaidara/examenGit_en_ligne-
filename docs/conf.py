"""
Configuration de la documentation Sphinx pour le projet examenGit_en_ligne
"""

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information --
project = 'examenGit_en_ligne'
copyright = '2026, khadijahaidara'
author = 'khadijahaidara'
release = '1.0.0'

# -- General configuration --
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output --
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Extension configuration --
# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
}

# -- Custom settings --
master_doc = 'index'
