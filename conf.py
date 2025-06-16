# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Peacock TV Activation Guide'
copyright = '2025, www.Peacocktv TV'
author = 'www.peacocktv.com tv'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages'  # Optional: enables .nojekyll on GitHub Pages
]

templates_path = ['_templates']
html_static_path = ['_static']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

html_title = "WWW.PeacockTV.com tv – Activate Peacock TV on Your Device"
html_short_title = "Peacock TV Activation"
html_favicon = 'favicon.ico'
html_show_sourcelink = False
html_allow_unsafe = True

# Theme settings removed to use default Sphinx or Read the Docs theme
# You may still override style using _static/custom.css if needed
