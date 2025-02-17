import os
import sys
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath('../../'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'asymintervals'
copyright = '2024, Wojciech Sałabun'
author = 'Wojciech Sałabun'
release = '1.1.1'

html_theme = 'furo'#'sphinx_rtd_theme'#'furo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon', 'sphinx_rtd_theme', 'sphinx.ext.autodoc']

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db',
                    '.DS_Store', '**.ipynb_checkpoints',
                    'requirements.txt']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_static_path = ['_static']


# # Configuration file for the Sphinx documentation builder.
# #
# # This file only contains a selection of the most common options. For a full
# # list see the documentation:
# # https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# # -- Path setup --------------------------------------------------------------
#
# # If extensions (or modules to document with autodoc) are in another directory,
# # add these directories to sys.path here. If the directory is relative to the
# # documentation root, use os.path.abspath to make it absolute, like shown here.
# #
# import os
# import sys
# import sphinx_rtd_theme
# from recommonmark.parser import CommonMarkParser
#
# sys.path.insert(0, os.path.abspath('../'))
#
# # -- Project information -----------------------------------------------------
#
# project = 'pymcdm'
# copyright = '2024, shekhand & kiziub'
# author = 'shekhand & kiziub'
#
# # -- General configuration ---------------------------------------------------
#
# # Add any Sphinx extension module names here, as strings. They can be
# # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# # ones.
# extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx_rtd_theme', 'myst_parser', 'nbsphinx',
#               'IPython.sphinxext.ipython_console_highlighting',
#               ]
#
# # DOBRE BYLO
# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.txt': 'markdown',
#     '.md': 'markdown',
# }
#

# # Mathematics expersions
# math_numfig = True
# numfig = True
# math_eqref_format = "{number}"
#
# # Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']
#
# # List of patterns, relative to source directory, that match files and
# # directories to ignore when looking for source files.
# # This pattern also affects html_static_path and html_extra_path.

#
# # Suppress warnings by MyST
# suppress_warnings = ["myst.xref_missing"]
#
# # -- Options for HTML output -------------------------------------------------
#
# # The theme to use for HTML and HTML Help pages.  See the documentation for
# # a list of builtin themes.
# #
# html_theme = "sphinx_rtd_theme"
#
# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
#
#
# def setup(app):
#     app.add_css_file('css/custom.css')


