# -*- coding: utf-8 -*-

import click
from .compat import StringIO
import seria


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--xml', 'out_fmt', flag_value='xml')
@click.option('--yaml', 'out_fmt', flag_value='yaml')
@click.option('--json', 'out_fmt', flag_value='json')
@click.argument('input', type=click.File('rb'), default='-')
@click.argument('output', type=click.File('wb'), default='-')
def cli(out_fmt, input, output):
    """Converts text."""
    _input = StringIO()
    for l in input:
        try:
            _input.write(str(l))
        except TypeError:
            _input.write(bytes(l, 'utf-8'))
    _serialized_obj = seria.load(_input)
    output.write(_serialized_obj.dump(out_fmt))


if __name__ == '__main__':
    cli(out_fmt, input, output)

