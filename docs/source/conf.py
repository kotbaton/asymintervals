import os
import sys

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
release = '1.0.0'

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


