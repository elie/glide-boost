#!/usr/bin/env python


from setuptools import setup

setup(
    name='Glide Rithm',
    version='1.5.0',
    description='Rithm themes for Glide.',
    author='Joel Burton',
    author_email='joel@joelburton.com',
    url='https://github.com/joelburton/glide-rithm',
    packages=['glide_rithm'],
    install_requires=["glide"],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'revealjs-rithm = glide_rithm',
            'handouts-rithm = glide_rithm',
        ],
    },
)
