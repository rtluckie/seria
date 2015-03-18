# -*- coding: utf-8 -*-

import sys

from .compat import StringIO
import seria

from docopt import docopt

docopt_args = """Seria - Serialization for humans

Usage:
  seria [-h]
  seria ([--json | -j ] | [--xml | -x] | [--yaml | -y]) (INPUT|"[-]")

Arguments:
  INPUT  Input stream for serialization.  Can be file stdin stream or uri
Options:
  -h --help             show this help message and exit
  -j --json             Output json
  -x --xml              Output xml
  -y --yaml             Output yaml
"""


def main():
    _serialized_obj = None
    args = docopt(docopt_args)

    if not args['INPUT']:
        print docopt_args
        return

    if args['INPUT'] != '-':
        with open(args['INPUT'], 'rb') as f:
            _serialized_obj = seria.load(f)

    elif args['INPUT'] == '-':
        _serialized_obj = StringIO()
        for l in sys.stdin:
            try:
                _serialized_obj.write(str(l))
            except TypeError:
                _serialized_obj.write(bytes(l, 'utf-8'))

        _serialized_obj = seria.load(_serialized_obj)

    if args['--json']:
        sys.stdout.write(_serialized_obj.dump('json'))
    if args['--xml']:
        sys.stdout.write(_serialized_obj.dump('xml'))
    if args['--yaml']:
        sys.stdout.write(_serialized_obj.dump('yaml'))


if __name__ == "__main__":
    main()
