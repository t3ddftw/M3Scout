#!/usr/bin/env python
import os
from setuptools import setup
from setuptools import find_packages

setup(
    name='m3scout',
    version='1.0',
    packages=find_packages(exclude=('tests',)),
)