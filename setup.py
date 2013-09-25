#!/usr/bin/env python
from distutils.core import setup
from setuptools import setup 
setup(name='Font Compare',
      version='1.0',
      description='FontForge based utility for aesthetic testing  of fonts',
      author='Mayank Jha',
      author_email='mayank25080562@gmail.com',
      url='https://github.com/mjnovice/FontCompare',
      include_package_data=True,
      packages=['fc'],
<<<<<<< HEAD
      package_data={'fc/data': ['data/*.mcy','data/*.bmp','data/*.png'],
      'fc/docs': ['docs/*.txt']},
=======
      package_data={'fc/docs': ['docs/*.txt']},
>>>>>>> cf0954c95baad4a87c7faa6f5a211f362523c54d
      scripts = ['fontcompare'],
      install_requires=[
      "Pillow >=2.0",
      ],
    )
