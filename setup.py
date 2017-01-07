# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mollie-rest-api-python',
    version='0.1.0',
    description='A Python Client for the Mollie REST API',
    long_description=long_description,
    url='https://github.com/Thijs-Riezebeek/mollie-rest-api-python',
    author='Mollie B.V.',
    author_email='info@mollie.nl',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='mollie psp payments rest api',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests',
    ]
)