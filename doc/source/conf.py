import sys
import os


sys.path.insert(0, os.path.abspath("../../"))

project = "pysyncon"
copyright = "2025, Stiofán Fordham"
author = "Stiofán Fordham"
release = "1.5.2"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinxcontrib.bibtex",
]
html_theme = "alabaster"
bibtex_bibfiles = ["biblio.bib"]
