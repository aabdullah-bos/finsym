import os
import re
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = ''
with open('financial_symbols/version.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

AUTHOR = 'Cargometrics Technologies'
EMAIL = 'aabdullah@cargometrics.com'
REQUIRES = ['singledispatch']

setup(
    name='financial_symbols',
    version=version,
    author=AUTHOR,
    author_email=EMAIL,
    packages=['financial_symbols'],
    package_data={'financial_symbols': ['README.md']},
    url='http://www.cargometrics.com',
    description='Package for representing financial symbols',
    long_description=read('README.md'),
    install_requires=REQUIRES
)
