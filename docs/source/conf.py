# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SOR Documentation'
copyright = '2022, System Overload Robotics'
author = 'SOR'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxext.remoteliteralinclude',
    'javasphinx3'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'karma_sphinx_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

javadoc_url_map = {
    "revrobotics" : ("https://codedocs.revrobotics.com/java/index.html", "javadoc8")
}