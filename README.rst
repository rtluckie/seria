Seria: Serialization for Humans
===============================
.. image:: https://img.shields.io/pypi/v/seria.svg
    :target: https://pypi.python.org/pypi/seria

.. image:: https://img.shields.io/pypi/dm/seria.svg
        :target: https://pypi.python.org/pypi/seria

.. image:: https://travis-ci.org/rtluckie/seria.svg?branch=master
    :target: https://travis-ci.org/rtluckie/seria

Basic Usage
-----------

.. code-block:: python

    import seria
    with open("tests/resources/good.xml", "rb") as f:
        s = seria.load(f)
        print s.dump('xml')
        print s.dump('json')
        print s.dump('yaml')

CLI Tool
-----------
Seria includes a useful command line tool.

.. code-block:: bash
    
    cat tests/resources/good.xml | seria -y -
    cat tests/resources/good.json | seria -j -
    cat tests/resources/good.yaml | seria -x -
    cat tests/resources/good.xml | seria -x - | seria -j - | seria -y -


Features
--------

- Support for (with a few limitations) json, yaml, xml

Installation
------------

.. code-block:: bash

    pip install seria