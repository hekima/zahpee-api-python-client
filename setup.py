import os
from setuptools import setup, find_packages


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
    url="http://www.zahpee.com",
    packages=find_packages(exclude=["test*"]),
    long_description=read('README.md'),
    test_suite="src.unittest",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        ],
    )
