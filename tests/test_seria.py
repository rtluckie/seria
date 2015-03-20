from seria import compat

import pytest

import os
test_resources = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')
from seria.compat import StringIO

import seria
from seria.serializers import get_formats, Serializer
from seria.providers import XML, YAML, JSON


class TestSeriaFuncs(object):
    def test_validate_xml_good(self):
        with open(os.path.join(test_resources, 'good.xml'), 'r') as f:
            _ = XML.is_it(f)
            assert _ == True

    def test_validate_xml_bad(self):
        with open(os.path.join(test_resources, 'bad.xml'), 'r') as f:
            _ = XML.is_it(f)
            assert _ == False

    def test_validate_json_good(self):
        with open(os.path.join(test_resources, 'good.json'), 'r') as f:
            _ = JSON.is_it(f)
            assert _ == True

    def test_validate_json_bad(self):
        with open(os.path.join(test_resources, 'bad.json'), 'r') as f:
            _ = JSON.is_it(f)
            assert _ == False

    def test_validate_yaml_good(self):
        with open(os.path.join(test_resources, 'good.yaml'), 'r') as f:
            _ = YAML.is_it(f)
            assert _ == True

    def test_validate_yaml_bad(self):
        with open(os.path.join(test_resources, 'bad.yaml'), 'r') as f:
            _ = YAML.is_it(f)
            assert _ == False

    def test_validate_yaml_with_good_json_input(self):
        """
        YAML is technically a superset of json, ie valid json == valid yaml
        """
        with open(os.path.join(test_resources, 'good.json'), 'r') as f:
            _ = YAML.is_it(f)
            assert _ == True

    def test_validate_yaml_with_bad_json_input(self):
        with open(os.path.join(test_resources, 'bad.json'), 'r') as f:
            _ = YAML.is_it(f)
            assert _ == False


    def test_get_format_with_good_json_input(self):
        with open(os.path.join(test_resources, 'good.json'), 'r') as f:
            _ = get_formats(f)
            assert _ == (True, False, True)

    def test_get_format_with_bad_json_input(self):
        with open(os.path.join(test_resources, 'bad.json'), 'r') as f:
            _ = get_formats(f)
            assert _ == (False, False, False)


    def test_get_format_with_good_yaml_input(self):
        with open(os.path.join(test_resources, 'good.yaml'), 'r') as f:
            _ = get_formats(f)
            assert _ == (False, False, True)

    def test_get_format_with_bad_yaml_input(self):
        with open(os.path.join(test_resources, 'bad.yaml'), 'r') as f:
            _ = get_formats(f)
            assert _ == (False, False, False)

    def test_get_format_with_good_xml_input(self):
        with open(os.path.join(test_resources, 'good.xml'), 'r') as f:
            _ = get_formats(f)
            assert _ == (False, True, False)

    def test_get_format_with_bad_xml_input(self):
        with open(os.path.join(test_resources, 'bad.xml'), 'r') as f:
            _ = get_formats(f)
            assert _ == (False, False, False)


class TestSeria(object):
    def test_get_formats_when_stream_changes(self):
        with open(os.path.join(test_resources, 'good.xml'), 'r') as f:
            _stream = seria.load(f)
        assert _stream.formats == (False, True, False)
        with open(os.path.join(test_resources, 'good.yaml'), 'r') as f:
            _stream = seria.load(f)
        assert _stream.formats == (False, False, True)

    def test_format_property_access(self):
        with open(os.path.join(test_resources, 'good.xml'), 'r') as f:
            _stream = seria.load(f)
            assert _stream.is_json == False
            assert _stream.is_xml == True
            assert _stream.is_yaml == False


class TestSeriaErrors(object):
    def test_input_must_be_flo(self):
        with pytest.raises(Serializer.Error):
            _ = seria.load("somestring")


class TestSeriaRoundTrips(object):
    def test_xml_to_json_to_xml(self):
        _source_fmt = 'xml'
        _target_fmt = 'json'
        with open(os.path.join(test_resources, 'good.%s' % _source_fmt), 'r') as _a:
            _a_seria = seria.load(_a)
            _b = StringIO()
            _b.write(_a_seria.dump(fmt=_target_fmt))
            _b_seria = seria.load(_b)
            _c = StringIO()
            _c.write(_b_seria.dump(fmt=_source_fmt, pretty=True, newl='\n', indent='    '))
            _c.seek(0)
            _a.seek(0)
            assert _a.read() == _c.read()

    def test_xml_to_yaml_to_xml(self):
        _source_fmt = 'xml'
        _target_fmt = 'yaml'
        with open(os.path.join(test_resources, 'good.%s' % _source_fmt), 'r') as _a:
            _a_seria = seria.load(_a)
            _b = StringIO()
            _b.write(_a_seria.dump(fmt=_target_fmt))
            _b_seria = seria.load(_b)
            _c = StringIO()
            _c.write(_b_seria.dump(fmt=_source_fmt, pretty=True, newl='\n', indent='    '))
            _c.seek(0)
            _a.seek(0)
            assert _a.read() == _c.read()

    # def test_json_to_xml_to_json(self):
    #     _source_fmt = 'json'
    #     _target_fmt = 'xml'
    #     with open(os.path.join(test_resources, 'good.%s' % _source_fmt), 'r') as _a:
    #         _a_seria = seria.load(_a)
    #         _b = StringIO()
    #         _b.write(_a_seria.dump(fmt=_target_fmt))
    #         _b_seria = seria.load(_b)
    #         _c = StringIO()
    #         _c.write(_b_seria.dump(fmt=_source_fmt))
    #         _a.seek(0)
    #         _c.seek(0)
    #         assert _a.read() == _c.read()

    # def test_json_to_yaml_to_json(self):
    #     _source_fmt = 'json'
    #     _target_fmt = 'yaml'
    #     with open(os.path.join(test_resources, 'good.%s' % _source_fmt), 'r') as _a:
    #         _a_seria = seria.load(_a)
    #         _b = StringIO()
    #         _b.write(_a_seria.dump(fmt=_target_fmt))
    #         _b_seria = seria.load(_b)
    #         _c = StringIO()
    #         _c.write(_b_seria.dump(fmt=_source_fmt))
    #         _a.seek(0)
    #         _c.seek(0)
    #         assert _a.read() == _c.read()

    def test_yaml_to_json_to_yaml(self):
        _source_fmt = 'yaml'
        _target_fmt = 'json'
        with open(os.path.join(test_resources, 'good.%s' % _source_fmt), 'r') as _a:
            _a_seria = seria.load(_a)
            _b = StringIO()
            _b.write(_a_seria.dump(fmt=_target_fmt))
            _b_seria = seria.load(_b)
            _c = StringIO()
            _c.write(_b_seria.dump(fmt=_source_fmt))
            _a.seek(0)
            _c.seek(0)
            assert _a.read() == _c.read()

    def test_yaml_to_xml_to_yaml(self):
        _source_fmt = 'yaml'
        _target_fmt = 'xml'
        with open(os.path.join(test_resources, 'good.%s' % _source_fmt), 'r') as _a:
            _a_seria = seria.load(_a)
            _b = StringIO()
            _b.write(_a_seria.dump(fmt=_target_fmt))
            _b_seria = seria.load(_b)
            _c = StringIO()
            _c.write(_b_seria.dump(fmt=_source_fmt))
            _a.seek(0)
            _c.seek(0)
            assert _a.read() == _c.read()