#!/usr/bin/env python
from distutils.core import setup

setup(name='Font Compare',
      version='1.0',
      description='FontForge based utility',
      author='Mayank Jha',
      author_email='mayank25080562@gmail.com',
      url='https://github.com/mjnovice/FontCompare',
      packages=['fc'],
      data_files = [('/usr/bin', ['fontcompare'])]
    )
