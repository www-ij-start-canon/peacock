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

# -- Meta tags for Google/Bing Webmaster verification and SEO ----------------

def setup(app):
    app.add_meta_tag("google-site-verification", "yIimRRNvbOiOrWRj8tgN-8fp39YM636FvhdQqCcfgbY")
    app.add_meta_tag("msvalidate.01", "4C170AB63B370E30D70955199A9A7B67")
    app.add_meta_tag("description", "Activate Peacock TV on your smart TV or streaming device at peacocktv.com/tv. Follow our step-by-step guide to enter your activation code and start streaming.")
    app.add_meta_tag("keywords", "peacocktv.com/tv, Peacock TV activation, activate Peacock TV, Peacock TV login, Peacock TV code entry, stream Peacock TV")
    app.add_meta_tag("robots", "index, follow")
