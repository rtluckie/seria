import os
try:
    from cStringIO import StringIO
except ImportError:
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

import pytest

import os
resources = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')


from seria import Seria, get_formats
from seria.providers import XML, YAML, JSON


class TestSeriaFuncs(object):
    def test_validate_xml_good(self):
        with open(os.path.join(resources, 'good.xml'), 'r') as f:
            _ = XML.is_it(f)
            assert _ == True

    def test_validate_xml_bad(self):
        with open(os.path.join(resources, 'bad.xml'), 'r') as f:
            _ = XML.is_it(f)
            assert _ == False

    def test_validate_json_good(self):
        with open(os.path.join(resources, 'good.json'), 'r') as f:
            _ = JSON.is_it(f)
            assert _ == True

    def test_validate_json_bad(self):
        with open(os.path.join(resources, 'bad.json'), 'r') as f:
            _ = JSON.is_it(f)
            assert _ == False

    def test_validate_yaml_good(self):
        with open(os.path.join(resources, 'good.yaml'), 'r') as f:
            _ = YAML.is_it(f)
            assert _ == True

    def test_validate_yaml_bad(self):
        with open(os.path.join(resources, 'bad.yaml'), 'r') as f:
            _ = YAML.is_it(f)
            assert _ == False

    def test_validate_yaml_with_good_json_input(self):
        """
        YAML is technically a superset of json, ie valid json == valid yaml
        """
        with open(os.path.join(resources, 'good.json'), 'r') as f:
            _ = YAML.is_it(f)
            assert _ == True

    def test_validate_yaml_with_bad_json_input(self):
        with open(os.path.join(resources, 'bad.json'), 'r') as f:
            _ = YAML.is_it(f)
            assert _ == False


    def test_get_format_with_good_json_input(self):
        with open(os.path.join(resources, 'good.json'), 'r') as f:
            _ = get_formats(f)
            assert _ == (True, False, True)

    def test_get_format_with_bad_json_input(self):
        with open(os.path.join(resources, 'bad.json'), 'r') as f:
            _ = get_formats(f)
            assert _ == (False, False, False)


    def test_get_format_with_good_yaml_input(self):
        with open(os.path.join(resources, 'good.yaml'), 'r') as f:
            _ = get_formats(f)
            assert _ == (False, False, True)

    def test_get_format_with_bad_yaml_input(self):
        with open(os.path.join(resources, 'bad.yaml'), 'r') as f:
            _ = get_formats(f)
            assert _ == (False, False, False)

    def test_get_format_with_good_xml_input(self):
        with open(os.path.join(resources, 'good.xml'), 'r') as f:
            _ = get_formats(f)
            assert _ == (False, True, False)

    def test_get_format_with_bad_xml_input(self):
        with open(os.path.join(resources, 'bad.xml'), 'r') as f:
            _ = get_formats(f)
            assert _ == (False, False, False)


class TestSeria(object):
    def test_input_must_be_flo(self):
        with pytest.raises(Seria.Error):
            _ = Seria("somestring")
    def test_get_formats_when_stream_changes(self):
        with open(os.path.join(resources, 'good.xml'), 'r') as f:
            _stream = Seria(f)
        assert _stream.formats == (False, True, False)
        with open(os.path.join(resources, 'good.yaml'), 'r') as f:
            _stream = Seria(f)
        assert _stream.formats == (False, False, True)

    def test_format_property_access(self):
        with open(os.path.join(resources, 'good.xml'), 'r') as f:
            _stream = Seria(f)
            assert _stream.is_json == False
            assert _stream.is_xml == True
            assert _stream.is_yaml == False


class TestSeria(object):
    def test_input_must_be_flo(self):
        with pytest.raises(Seria.Error):
            _ = Seria("somestring")


class TestSeriaRoundTrips(object):
    def test_xml_to_json_to_xml(self):
        with open(os.path.join(resources, 'good.xml'), 'r') as _original_xml_flo:
            _original_xml_Seria = Seria(_original_xml_flo)
            _json_flo = StringIO()
            _json_flo.write(_original_xml_Seria.dump(fmt='json'))
            _json_Seria = Seria(_json_flo)
            _new_xml_flo = StringIO()
            _new_xml_flo.write(_json_Seria.dump(fmt='xml', pretty=True, newl='\n', indent='    '))
            _new_xml_flo.seek(0)
            _original_xml_flo.seek(0)
            assert _original_xml_flo.read() == _new_xml_flo.read()