#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == '__main__':
    setup(name='zahpeeapi',
          version='0.0.8',
          description='Zahpee API Python Client',
          long_description=read('README.md'),
          author="Zahpee Dev Team",
          author_email="contato@zahpee.com",
          license='MIT',
          url="http://www.zahpee.com",
          scripts=[],
          packages=find_packages('src/main/python'),
          package_dir={'': 'src/main/python'},
          classifiers=['Development Status :: 3 - Alpha', 'Programming Language :: Python'],
          entry_points={
              'console_scripts': []
          },
          zip_safe=True)
