#!/usr/bin/env python

from setuptools import setup, find_packages

with open('fs_cellarfs/_version.py') as f:
    exec(f.read())

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: System :: Filesystems',
]

with open('README.rst', 'rt') as f:
    DESCRIPTION = f.read()

REQUIREMENTS = [
    "fs-s3fs~=1.0"
]

setup(
    name='fs-cellarfs',
    author="Damien Thirion",
    author_email="thirion.damien@gmail.com",
    classifiers=CLASSIFIERS,
    description="Clever-Cloud S3 Cellar filesystem for PyFilesystem2",
    install_requires=REQUIREMENTS,
    license="MIT",
    long_description=DESCRIPTION,
    packages=find_packages(),
    keywords=['pyfilesystem', 's3', 'clever-cloud', 'cellar'],
    platforms=['any'],
    url="",
    version=__version__,
    entry_points={'fs.opener': [
         'cellar = fs_cellarfs.opener:CellarFSOpener',
    ]},
)
