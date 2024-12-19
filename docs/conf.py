# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'prospero-docs'
copyright = '2020-, Liverpool John Moores University'
author = 'Robert Crain, Kenny Andersson'
version = release = '4.16'

# -- General configuration ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]
extensions = []
language = 'en'
master_doc = 'index'
pygments_style = 'sphinx'
source_suffix = '.rst'
templates_path = ['_templates']

# -- Options for HTML output ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
