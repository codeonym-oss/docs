"""Sphinx configuration of docs.codeonym.work: the hub of codeonym's project docs."""

project = "codeonym docs"
author = "codeonym"
copyright = "codeonym"

extensions = ["myst_parser"]
exclude_patterns = ["_build"]

html_theme = "shibuya"
html_title = "codeonym docs"
html_baseurl = "https://docs.codeonym.work/"
html_theme_options = {
    "accent_color": "indigo",
    "github_url": "https://github.com/codeonym-oss",
}
