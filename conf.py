# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Peacock TV Activation Guide'
copyright = '2025, Peacock TV'
author = 'Peacock TV, NBCUniversal Media, LLC'

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

html_theme = 'furo'
html_title = "WWW.PeacockTV.com tv – Activate Peacock TV on Your Device"
html_short_title = "Peacock TV Activation"
html_favicon = 'favicon.ico'
html_show_sourcelink = False
html_allow_unsafe = True

html_theme_options = {
    'show_powered_by': False,
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
}

# -- Remove the invalid setup() function --
