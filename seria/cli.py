import sys

try:
    from cStringIO import StringIO
except ImportError:
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

from docopt import docopt

from seria import Seria

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
    if args['INPUT'] != '-':
        with open(args['INPUT'], 'rb') as f:
            _serialized_obj = Seria(f)

    elif args['INPUT'] == '-':
        _serialized_obj = StringIO()
        for l in sys.stdin:
            _serialized_obj.write(l)
        _serialized_obj = Seria(_serialized_obj)

    if args['--json']:
        sys.stdout.write(_serialized_obj.dump('json'))
    if args['--xml']:
        sys.stdout.write(_serialized_obj.dump('xml'))
    if args['--yaml']:
        sys.stdout.write(_serialized_obj.dump('yaml'))


if __name__ == "__main__":
    main()
