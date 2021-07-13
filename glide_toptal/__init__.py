from os import path

version = "1.5.0"


def setup(app):
    app.add_html_theme(
        'revealjs-toptal',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "revealjs-toptal")))
    app.add_html_theme(
        'handouts-toptal',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "handouts-toptal")))
