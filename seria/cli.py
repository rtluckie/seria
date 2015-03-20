# -*- coding: utf-8 -*-

import click
from .compat import StringIO, str, builtin_str
import seria


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--xml', 'out_fmt', flag_value='xml')
@click.option('--yaml', 'out_fmt', flag_value='yaml')
@click.option('--json', 'out_fmt', flag_value='json')
@click.argument('input', type=click.File('r'), default='-')
@click.argument('output', type=click.File('w'), default='-')
def cli(out_fmt, input, output):
    """Converts text."""
    _input = StringIO()
    for l in input:
        try:
            _input.write(str(l))
        except TypeError:
            _input.write(bytes(l, 'utf-8'))
    _input = seria.load(_input)
    _out = (_input.dump(out_fmt))
    output.write(_out)


if __name__ == '__main__':
    cli(out_fmt, input, output)