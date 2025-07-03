# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate My5 TV'
copyright = '2025, Activate My5 TV'
author = 'Activate My5 TV'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Activate My5 TV on Your Device – Step-by-Step Guide"

# Optional short title (e.g., for nav bar)
html_short_title = "Activate My5 TV Guide"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme (you can uncomment if you want)
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source" link at the bottom
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Enable raw directive globally
raw_enabled = True

# Paths to templates and static files (uncomment if you have any)
templates_path = ['_templates']
# html_static_path = ['_static']

# Patterns to ignore when looking for source files
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
