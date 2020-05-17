# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='gimpformats',
    version='2020.2.4',
    description='Pure python implementation of the gimp file format(s)',
    python_requires='==3.*,>=3.5.0',
    project_urls={
        "documentation":
            "https://github.com/FHPythonUtils/GimpFormats/blob/master/README.md",
        "homepage":
            "https://github.com/FHPythonUtils/GimpFormats",
        "repository":
            "https://github.com/FHPythonUtils/GimpFormats"
    },
    author='FredHappyface',
    classifiers=[
        'Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English', 'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    packages=['gimpFormats'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'binaryiotools==2020.*,>=2020.1.1', 'blendmodes==2020.*,>=2020.2.2',
        'brackettree==0.*,>=0.2.5', 'numpy==1.*,>=1.18.4', 'pillow==7.*,>=7.1.2'
    ],
)
