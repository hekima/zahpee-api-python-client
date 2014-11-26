import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Zahpee API Python Client',
    version="0.0.1",
    author="Zahpee",
    author_email="contato@zahpee.com",
    description="Zahpee API Python Client",
    license="MIT",
    keywords="zahpee api python",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['src', 'unittest'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        ],
    )
