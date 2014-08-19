# setup
# Setup and build script for Allusive
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sun Aug 17 13:08:50 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: setup.py [] benjamin@bengfort.com $

"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

##########################################################################
## Imports
##########################################################################

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    raise ImportError("Could not import \"setuptools\"."
                      "Please install the setuptools package.")

##########################################################################
## Package Information
##########################################################################

## Discover packages
packages = find_packages(where=".", exclude=("tests", "bin", "docs", "fixtures"))

## Load the requirements
requires = []
with open('requirements.txt', 'r') as reqfile:
    for line in reqfile:
        requires.append(line.strip())
requires.append("py2app")

## Define the classifiers
classifiers = (
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Utilities',
)

## Define the keywords
keywords = ('secret', 'quicksilver', 'cipher', 'text editor')

## Define the description
long_description = ""

## Define the application
app = ['bin/Allusive.py']

## Define data files
data_files = ['--iconfile']

## Define py2app options
options= {
    'py2app': {
        'argv_emulation': True,
        'iconfile': '/Users/benjamin/Repos/git/allusive-editor/assets/top_secret.icns',
    }
}

## Define the configuration
config = {
    "app": app,
    "name": "Allusive Editor",
    "version": "0.1.0",
    "description": "A text editor that implements Neal Stephenson's cipher in Quicksilver",
    "long_description": long_description,
    "license": "MIT",
    "author": "Benjamin Bengfort",
    "author_email": "benjamin@bengfort.com",
    "url": "https://github.com/bbengfort/allusive-editor",
    "download_url": 'https://github.com/bbengfort/allusive-editor/tarball/v0.1.0',
    "packages": packages,
    "install_requires": requires,
    "setup_requires": requires,
    "classifiers": classifiers,
    "keywords": keywords,
    "zip_safe": True,
    "scripts": [],
    "options": options,
    "data_files": data_files,
}

if __name__ == '__main__':
    setup(**config)
