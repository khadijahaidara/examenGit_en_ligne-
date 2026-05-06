"""
Setup script pour le projet examenGit_en_ligne
"""

from setuptools import setup, find_packages
import os

# Lecture du README.md
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Lecture des requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="examen-git-en-ligne",
    version="1.0.0",
    author="khadijahaidara",
    author_email="khadijahaidara@example.com",
    description="Jeu de devinette de nombre avec fonctions utilitaires et tests complets",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/khadijahaidara/examenGit_en_ligne-",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Environment :: X11 Applications :: Qt",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "sphinx-autodoc-typehints>=1.19.0",
        ],
        "gui": [
            "tkinter",  # Généralement inclus avec Python
        ],
    },
    entry_points={
        "console_scripts": [
            "jeu-devinette=src.game.game:main",
            "jeu-devinette-gui=src.gui.game_gui:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.txt", "*.md"],
    },
    data_files=[
        ("share/examen-git-en-ligne/docs", ["docs/installation.rst", "docs/api.rst"]),
        ("share/examen-git-en-ligne/examples", ["examples/basic_usage.py"]),
    ],
    zip_safe=False,
    keywords="game, guessing, education, tkinter, cli, utilities",
    project_urls={
        "Bug Reports": "https://github.com/khadijahaidara/examenGit_en_ligne-/issues",
        "Source": "https://github.com/khadijahaidara/examenGit_en_ligne-",
        "Documentation": "https://examen-git-en-ligne.readthedocs.io/",
    },
)
