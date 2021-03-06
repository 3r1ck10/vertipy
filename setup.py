# Copyright 2020 by Erick Alexis Alvarez Sanchez, The national meteorological and hydrological service of Peru (SENAMHI).
# All rights reserved.
# This file is part of the VERTIpy package,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from setuptools import setup

setup(
    name='vertipy',
    version='1.0.0.2',
    description='Primera version de vertipy!',
    packages = ['vertipy'],
    license='MIT',
    author_email='erick.alvarez.met@gmail.com',
    download_url='https://github.com/3r1ck10/vertipy/archive/v1.0.0.2.tar.gz',
    install_requires=['numpy',
    'matplotlib','xarray','netcdf4'],
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
