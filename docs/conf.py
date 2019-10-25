# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Project information -----------------------------------------------------

project = 'Treelog'
copyright = '2018, Evalf'
author = 'Evalf'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.napoleon',
]

# -- Options for HTML output -------------------------------------------------

html_theme = 'default'
html_favicon = 'favicon.ico'
html_static_path = ['_static']
