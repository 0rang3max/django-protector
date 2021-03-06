# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath(".."))
import protector

master_doc = "index"
project = "Django-protector"
copyright = u'2015'
version = release = protector.__version__

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

intersphinx_mapping = {
    'python': ('http://python.readthedocs.org/en/latest/', None),
}

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# On RTD we can't import sphinx_rtd_theme, but it will be applied by
# default anyway.  This block will use the same theme when building locally
# as on RTD.
if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

