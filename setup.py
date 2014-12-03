#!/usr/bin/env python

from setuptools import setup,find_packages

if __name__ == '__main__':
    setup(
          name = 'zahpeeapi',
          version = '0.0.6',
          description = '''''',
          long_description = '''<class 'pybuilder.core.description'>''',
          author = "",
          author_email = "",
          license = '',
          url = '',
          scripts = [],
          packages = find_packages('src/main/python'),
          package_dir = {'':'src/main/python'},
          classifiers = ['Development Status :: 3 - Alpha', 'Programming Language :: Python'],
          entry_points={
          'console_scripts':
              []
          },
             #  data files
             # package data


          zip_safe=True
    )
