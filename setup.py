#!/usr/bin/env python
from distutils.core import setup
from setuptools import setup 
setup(name='Font Compare',
      version='1.0',
      description='FontForge based utility for aesthetic testing  of fonts',
      author='Mayank Jha',
      author_email='mayank25080562@gmail.com',
      url='https://github.com/mjnovice/FontCompare',
      packages=['fc'],
      scripts = ['fontcompare'],
      install_requires=[
      "Pillow >=2.0",
      ],
    )
