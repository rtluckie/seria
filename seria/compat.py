# -*- coding: utf-8 -*-

import sys

_ver = sys.version_info
is_py2 = (_ver[0] == 2)
is_py3 = (_ver[0] == 3)

try:
    import simplejson as json
except (ImportError, SyntaxError):
    import json

if is_py2:
    from StringIO import StringIO

    try:
        from collections import OrderedDict
    except ImportError:
        try:
            from ordereddict import OrderedDict
        except ImportError:
            OrderedDict = dict

    basestring = basestring
    builtin_str = str
    bytes = str
    str = unicode


elif is_py3:
    from io import StringIO
    from collections import OrderedDict

    basestring = (str, bytes)
    builtin_str = str
    bytes = bytes
    str = str