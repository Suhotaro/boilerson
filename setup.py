#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from pkg_resources import parse_requirements
from setuptools import find_packages, setup


def read(file_name):
    pkg_root_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(pkg_root_dir, file_name)
    assert os.path.isfile(file_path), f'setup.py cannot open not existing file: {file_path}'
    with open(file_path) as file_:
        return file_.read()


def get_requirements():
    return [str(r) for r in parse_requirements(read('requirements.txt'))]


setup(
    name='boilersson',
    url='https://code.falcon.lab/kestrel-dev/python-utils/boilersson',
    author='Falcon V Systems S.A.',
    author_email='FALCONDELIVERYTeam@vector.net',
    use_scm_version=True,
    description="Abstract boilerplate for new Falcon's python package projects",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=get_requirements(),
    setup_requires=['setuptools_scm'],
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],
    dependency_links=[
        "https://pypi.python.org/simple",
        "http://pypi.falcon.lab:4040/falcon/stable",
        "http://pypi.falcon.lab:4040/falcon/staging",
    ],
)
