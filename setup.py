# -*- coding: utf-8 -*-

import re
import ast

from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('frddy/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

try:
    with open('README.rst', 'r') as f:
        readme = f.read()
    with open('CHANGELOG.rst', 'r') as f:
        changelog = f.read()
except IOError:
    readme = ''
    changelog = ''

setup(
    name='frddy',
    author='Aaron Toth',
    version=version,
    url='https://github.com/aaront/frddy',
    description='',
    long_description=readme + '\n\n' + changelog,
    test_suite="tests",
    include_package_data=True,
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    package_dir={'frddy': 'frddy'},
    license='Apache 2.0',
    install_requires=[],
    entry_points='''
        [console_scripts]
        myg=frddy.cli:main
    ''',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries'
    ),
)
