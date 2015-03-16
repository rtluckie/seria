# -*- coding: utf-8 -*-

from xml.etree import ElementTree as ET

import xmltodict
import yaml

from .compat import str, basestring, OrderedDict, json, builtin_str
from .utils import str_to_num, set_defaults


class JSON(object):
    @staticmethod
    def validate_json(stream):
        stream.seek(0)
        try:
            json.loads(str(stream.read()))
            return True
        except ValueError:
            return False

    @staticmethod
    def is_it(stream):
        stream.seek(0)
        return JSON.validate_json(stream)

    @staticmethod
    def load(stream):
        stream.seek(0)
        return JSON.ordered_load(stream)

    @staticmethod
    def dump(obj, *args, **kwargs):
        defaults = {'indent': 4}
        set_defaults(kwargs, defaults)
        return json.dumps(obj, *args, **kwargs)

    @staticmethod
    def ordered_load(stream):
        return json.load(stream, object_pairs_hook=OrderedDict)


class XML(object):
    @staticmethod
    def validate_xml(stream):
        stream.seek(0)
        # TODO: Support for standard xml validation mechanisms
        _ = ET.parse(stream)

    @staticmethod
    def is_it(stream):
        stream.seek(0)
        try:
            XML.validate_xml(stream)
            return True
        except ET.ParseError:
            return False


    @staticmethod
    def load(stream):
        stream.seek(0)
        serialized = XML.ordered_load(stream)
        if 'SERIAROOT' in serialized:
            serialized = serialized['SERIAROOT']
        return serialized

    @staticmethod
    def dump(obj, *args, **kwargs):
        defaults = {"pretty": True, "newl": '\n', "indent": '    '}
        set_defaults(kwargs, defaults)
        if len(obj.keys()) > 1:
            obj = OrderedDict({"SERIAROOT": obj})
        return XML.ordered_dump(obj, *args, **kwargs)


    @staticmethod
    def ordered_load(stream, *args, **kwargs):
        defaults = {'postprocessor': XML.postprocessor}
        set_defaults(kwargs, defaults)
        return xmltodict.parse(stream.read(), *args, **kwargs)

    @staticmethod
    def ordered_dump(data, *args, **kwargs):
        return xmltodict.unparse(data, *args, **kwargs)

    @staticmethod
    def postprocessor(path, key, value):
        try:
            if isinstance(key, basestring):
                key = str(key)
            if isinstance(value, basestring):
                value = str(value)
            value = str_to_num(value)
            return key, value
        except (ValueError, TypeError):
            return key, value


class YAML(object):
    @staticmethod
    def validate_yaml(stream):
        stream.seek(0)
        try:
            _ = yaml.load(stream)
            # All strings, as long as they don't violate basic yaml guidelines, are valid yaml.
            # This is problematic because valid xml (and in some cases invalid xml) are considered valid yaml.
            # ie a yaml document that contains a string
            # For now, we are uninterested in yaml docs that contain merely a string.
            # TODO: Better detection of valid yaml
            if isinstance(_, (str, builtin_str)):
                return False
            return True
        except (yaml.parser.ParserError, yaml.scanner.ScannerError) as e:
            return False

    @staticmethod
    def is_it(stream):
        stream.seek(0)
        return YAML.validate_yaml(stream)

    @staticmethod
    def load(stream):
        stream.seek(0)
        return YAML.ordered_load(stream)

    @staticmethod
    def dump(serialized, *args, **kwargs):
        defaults = {"default_flow_style": False}
        set_defaults(kwargs, defaults)
        return YAML.ordered_dump(serialized, Dumper=yaml.SafeDumper, *args, **kwargs)


    @staticmethod
    def ordered_load(stream, Loader=yaml.SafeLoader, object_pairs_hook=OrderedDict):
        class OrderedLoader(Loader):
            pass

        def construct_mapping(loader, node):
            loader.flatten_mapping(node)
            return object_pairs_hook(loader.construct_pairs(node))

        OrderedLoader.add_constructor(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            construct_mapping)
        return yaml.load(stream, OrderedLoader)

    @staticmethod
    def ordered_dump(obj, stream=None, Dumper=yaml.Dumper, **kwargs):
        class OrderedDumper(Dumper):
            pass

        def _dict_representer(dumper, data):
            return dumper.represent_mapping(
                yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                data.items())

        OrderedDumper.add_representer(OrderedDict, _dict_representer)
        return yaml.dump(obj, stream, OrderedDumper, **kwargs)