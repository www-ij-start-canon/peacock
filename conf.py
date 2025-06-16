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

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "PeacockTV.com/tv – Activate Peacock TV on Your Device"

# Optional short title (e.g., for nav bar)
html_short_title = "Peacock TV Activation"

# Favicon (must be placed inside _static or root directory)
html_favicon = 'favicon.ico'

# Theme (use Furo or uncomment another theme like ReadTheDocs if needed)
html_theme = 'furo'

# Hide "View page source" links
html_show_sourcelink = False

# Allow raw HTML in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
}

# Paths to templates and static files
templates_path = ['_templates']
html_static_path = ['_static']

# Add extra files like Google verification HTML if needed
# html_extra_path = ['google12345abcde.html']

# Files or directories to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
