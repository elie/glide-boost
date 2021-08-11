from os import path

version = "1.5.0"


def setup(app):
    app.add_html_theme(
        'revealjs-boost',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "revealjs-boost")))
    app.add_html_theme(
        'handouts-boost',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "handouts-boost")))
