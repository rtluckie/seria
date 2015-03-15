Seria: Serialization for Humans
=========================


Basic Usage
-----------

.. code-block:: python
    with open("tests/resources/good.xml", "rb") as f:
        s = Seria(f)
        print s.dump('xml')
        print s.dump('json')
        print s.dump('yml')

CLI Tool
-----------
Seria includes a useful command line tool.

.. code-block:: bash
    cat tests/resources/good.xml | seria -y
    cat tests/resources/good.json | seria -j
    cat tests/resources/good.yaml | seria -x
    cat tests/resources/good.xml | seria -x - | seria -j - | seria -y
    ...

Features
--------

- Support for (with a few limitations) json, yaml, xml

Installation
------------

.. code-block:: bash

    pip install seria