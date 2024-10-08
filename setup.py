import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pywhitakers",
    version = "0.0.14",
    author = "Forrest Zeng",
    author_email = "forrestzengmusic@gmail.com",
    description = ("An API package to latin-words.com that returns the most likely Latin translation of a word."),
    license = "Apache 2.0",
    keywords = "Latin translation whitakers",
    long_description=read('README.md'),
    packages=find_packages(),
    install_requires=read("requirements.txt").splitlines()
)