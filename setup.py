#!/usr/bin/env python

from __future__ import with_statement

from setuptools import setup
import sys

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

# TODO: Add readme
with open('README.rst') as f:
    readme = f.read()
# TODO: add long description
long_description = "%s" % (readme)

packages = [
    'seria',
    ]
install_requires = [
    'PyYAML>=3.11',
    'xmltodict>=0.9.2',
    'click>=3.3',
    ]

setup(
    name='seria',
    version='0.1.5',
    description='Serialization for Humans',
    long_description=long_description,
    author='Ryan Luckie',
    author_email='rtluckie@gmail.com',
    url='https://github.com/rtluckie/seria',
    packages=packages,
    platforms=['all'],
    tests_require=['pytest', 'mock'],
    cmdclass = {'test': PyTest},
    install_requires=install_requires,
    package_dir={'seria': 'seria'},
    license='MIT',
    keywords='yaml json yaml yml serialize serialization deserialize deserialization cli',
    entry_points={
        'console_scripts': [
            'seria = seria.cli:cli',
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
