from os import path

version = "1.5.0"


def setup(app):
    app.add_html_theme(
        'revealjs-rithm',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "revealjs-rithm")))
    app.add_html_theme(
        'handouts-rithm',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "handouts-rithm")))
