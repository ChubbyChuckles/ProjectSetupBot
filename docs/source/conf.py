import os
import sys

sys.path.insert(0, os.path.abspath("../.."))  # Adjust to point to your project root

extensions = [
    "sphinx.ext.autodoc",  # For documenting Python code
    "sphinx.ext.napoleon",  # For Google/NumPy-style docstrings
    "sphinx.ext.viewcode",  # For linking to source code
]

html_theme = "sphinx_rtd_theme"
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "project-template"
copyright = "2025, Christian Rickert"
author = "Christian Rickert"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
