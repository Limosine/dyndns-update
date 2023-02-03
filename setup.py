
from setuptools import setup

setup(
    name='dyndns-update',
    version='20230129',
    description='Update your DynDNS hosts',
    author='Quentin Frey',
    author_email='quentin.frey@proton.me',
    url='https://github.com/Limosine/dyndns-update',
    packages=['dyndns_update'],
    install_requires=[
        'requests',
    ],
)
