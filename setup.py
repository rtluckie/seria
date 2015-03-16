#!/usr/bin/env python

from __future__ import with_statement

from setuptools import setup


# TODO: Add readme
with open('README.rst') as f:
    readme = f.read()
# TODO: add long description
long_description = """
Long Description
----
%s
----
""" % (readme)

packages = [
    'seria',
    ]
install_requires = [
    'docopt==0.6.2',
    'PyYAML==3.11',
    'xmltodict==0.9.0',
]

test_requires = [
    'mock==1.0.1',
    'pytest==2.5.2',
]
setup(
    name='seria',
    version='0.1.0',
    description='DESCRIPTION',
    long_description=long_description,
    author='Ryan Luckie',
    author_email='rtluckie@gmail.com',
    url='https://github.com/rtluckie/seria',
    packages=packages,
    platforms=['all'],
    tests_require=['pytest', 'mock'],
    install_requires=install_requires,
    package_dir={'seria': 'seria'},
    license='MIT',
    keywords='yaml json yaml yml serialize serialization deserialize deserialization cli',
    entry_points={
        'console_scripts': [
            'seria = seria.cli:main',
        ]
    },
    classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Utilities',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Systems Administration',
    ],
)