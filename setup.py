#!/usr/bin/env python


from setuptools import setup

setup(
    name='Glide Toptal',
    version='1.5.0',
    description='toptal themes for Glide.',
    author='Joel Burton',
    author_email='joel@joelburton.com',
    url='https://github.com/joelburton/glide-toptal',
    packages=['glide_toptal'],
    install_requires=["glide"],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'revealjs-toptal = glide_toptal',
            'handouts-toptal = glide_toptal',
        ],
    },
)
