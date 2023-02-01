
from setuptools import setup

setup(
    name='dyndns-update',
    version='20230129',
    description='Update your DynDNS hosts',
    author='Quentin Frey',
    author_email='***REMOVED***',
    url='https://github.com/Limosine/dyndns-update',
    packages=['dyndns_update'],
    install_requires=[
        'requests',
    ],
)
