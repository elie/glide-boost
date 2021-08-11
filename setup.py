#!/usr/bin/env python


from setuptools import setup

setup(
    name='Glide boost',
    version='1.5.0',
    description='boost themes for Glide.',
    author='Joel Burton',
    author_email='joel@joelburton.com',
    url='https://github.com/joelburton/glide-boost',
    packages=['glide_boost'],
    install_requires=["glide"],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'revealjs-boost = glide_boost',
            'handouts-boost = glide_boost',
        ],
    },
)
