import os

import click
from click.testing import CliRunner

import seria
from seria import cli

import click
from click.testing import CliRunner

test_resources = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')

runner = CliRunner()
class TestSeriaCLI(object):
    def test_cli_xml_to_xml_to_stdout(self):
        _input_fmt = 'xml'
        _output_fmt = 'xml'
        result = runner.invoke(cli.cli, ['--%s' % (_output_fmt), "%s/good.%s" % (test_resources, _input_fmt)], '-')
        with open("%s/good.%s" % (test_resources, _input_fmt), 'rb') as f:
            _s = seria.load(f)
            _comp_val = _s.dump(_output_fmt)
        assert result.exit_code == 0
        assert result.output == _comp_val


    def test_cli_xml_to_json_to_stdout(self):
        _input_fmt = 'xml'
        _output_fmt = 'json'
        result = runner.invoke(cli.cli, ['--%s' % (_output_fmt), "%s/good.%s" % (test_resources, _input_fmt)], '-')
        with open("%s/good.%s" % (test_resources, _input_fmt), 'rb') as f:
            _s = seria.load(f)
            _comp_val = _s.dump(_output_fmt)
        assert result.exit_code == 0
        assert result.output == _comp_val


    def test_cli_xml_to_yaml_to_stdout(self):
        _input_fmt = 'xml'
        _output_fmt = 'yaml'
        result = runner.invoke(cli.cli, ['--%s' % (_output_fmt), "%s/good.%s" % (test_resources, _input_fmt)], '-')
        with open("%s/good.%s" % (test_resources, _input_fmt), 'rb') as f:
            _s = seria.load(f)
            _comp_val = _s.dump(_output_fmt)
        assert result.exit_code == 0
        assert result.output == _comp_val


    def test_cli_json_to_json_to_stdout(self):
        _input_fmt = 'json'
        _output_fmt = 'json'
        result = runner.invoke(cli.cli, ['--%s' % (_output_fmt), "%s/good.%s" % (test_resources, _input_fmt)], '-')
        with open("%s/good.%s" % (test_resources, _input_fmt), 'rb') as f:
            _s = seria.load(f)
            _comp_val = _s.dump(_output_fmt)
        assert result.exit_code == 0
        assert result.output == _comp_val

    def test_cli_json_to_xml_to_stdout(self):
        _input_fmt = 'json'
        _output_fmt = 'xml'
        result = runner.invoke(cli.cli, ['--%s' % (_output_fmt), "%s/good.%s" % (test_resources, _input_fmt)], '-')
        with open("%s/good.%s" % (test_resources, _input_fmt), 'rb') as f:
            _s = seria.load(f)
            _comp_val = _s.dump(_output_fmt)
        assert result.exit_code == 0
        assert result.output == _comp_val


    def test_cli_json_to_yaml_to_stdout(self):
        _input_fmt = 'json'
        _output_fmt = 'yaml'
        result = runner.invoke(cli.cli, ['--%s' % (_output_fmt), "%s/good.%s" % (test_resources, _input_fmt)], '-')
        with open("%s/good.%s" % (test_resources, _input_fmt), 'rb') as f:
            _s = seria.load(f)
            _comp_val = _s.dump(_output_fmt)
        assert result.exit_code == 0
        assert result.output == _comp_val

    def test_cli_yaml_to_yaml_to_stdout(self):
        _input_fmt = 'yaml'
        _output_fmt = 'yaml'
        result = runner.invoke(cli.cli, ['--%s' % (_output_fmt), "%s/good.%s" % (test_resources, _input_fmt)], '-')
        with open("%s/good.%s" % (test_resources, _input_fmt), 'rb') as f:
            _s = seria.load(f)
            _comp_val = _s.dump(_output_fmt)
        assert result.exit_code == 0
        assert result.output == _comp_val

    def test_cli_yaml_to_json_to_stdout(self):
        _input_fmt = 'yaml'
        _output_fmt = 'json'
        result = runner.invoke(cli.cli, ['--%s' % (_output_fmt), "%s/good.%s" % (test_resources, _input_fmt)], '-')
        with open("%s/good.%s" % (test_resources, _input_fmt), 'rb') as f:
            _s = seria.load(f)
            _comp_val = _s.dump(_output_fmt)
        assert result.exit_code == 0
        assert result.output == _comp_val

    def test_cli_yaml_to_xml_to_stdout(self):
        _input_fmt = 'yaml'
        _output_fmt = 'xml'
        result = runner.invoke(cli.cli, ['--%s' % (_output_fmt), "%s/good.%s" % (test_resources, _input_fmt)], '-')
        with open("%s/good.%s" % (test_resources, _input_fmt), 'rb') as f:
            _s = seria.load(f)
            _comp_val = _s.dump(_output_fmt)
        assert result.exit_code == 0
        assert result.output == _comp_val