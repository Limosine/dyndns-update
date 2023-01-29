
from setuptools import setup

setup(
    name='dyndns-update',
    version='20230129',
    description='Update DynDNS hosts.',
    author='Quentin Frey',
    author_email='***REMOVED***',
    packages=['dyndns_update'],
    install_requires=[
        'requests',
    ],
)
