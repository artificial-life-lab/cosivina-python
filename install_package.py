#!/usr/bin/env python3
# flake8: noqa
'''
Setup script for the repository.
'''
from setuptools import find_packages, setup, Distribution
from cosivina.version import __version__

setup(
    name = 'cosivina',
    version = __version__,
    description='Compose, Simulate and Visualize Neurodynamic Architectures (COSIVINA)',
    author='Pranjal Dhole',
    author_email='dhole.pranjal@gmail.com',
    distclass = Distribution,
    packages = find_packages(),
    zip_safe = False,
)