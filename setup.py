#!/usr/bin/env python3

from setuptools import setup

setup(
    name='dyndns-update',
    version='20230205',
    description='Update your DynDNS hosts',
    author='Quentin Frey',
    author_email='quentin.frey@proton.me',
    url='https://github.com/Limosine/dyndns-update',
    packages=['dyndns_update'],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'dyndns-update=dyndns_update:command_line',
        ],
    },
)
