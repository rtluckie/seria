# -*- coding: utf-8 -*-

from .providers import (
    XML,
    JSON,
    YAML,
)


def get_formats(stream):
    fmts = []
    for _fmt in [JSON, XML, YAML]:
        stream.seek(0)
        fmts.append(_fmt.is_it(stream))
    return tuple(fmts)


class Serializer(object):
    class Error(Exception):
        pass

    def __init__(self, stream):
        self.stream = stream
        self.formats = get_formats(self.stream)

    @property
    def stream(self):
        return self._stream

    @stream.setter
    def stream(self, stream):
        if not (hasattr(stream, 'read') or hasattr(stream, 'getvalue')):
            raise Serializer.Error("Stream must be file-like object")
        self._stream = stream
        self.formats = get_formats(self.stream)
        self.serialized = self.load()

    @property
    def is_json(self):
        return self.formats[0]

    @property
    def is_xml(self):
        return self.formats[1]

    @property
    def is_yaml(self):
        return self.formats[2]

    def dump(self, fmt, *args, **kwargs):
        if fmt == 'yaml':
            return YAML.dump(self.serialized, *args, **kwargs)
        elif fmt == 'json':
            return JSON.dump(self.serialized, *args, **kwargs)
        elif fmt == 'xml':
            return XML.dump(self.serialized, *args, **kwargs)
        else:
            raise Serializer.Error("Requested format '%s' is not a supported format" % fmt)

    def load(self):
        if self.is_xml:
            return XML.load(self._stream)
        elif self.is_yaml:
            return YAML.load(self._stream)
        # No need for JSON.load since yaml is a superset of json
        else:
            raise Serializer.Error("Input does not appear to be a supported format")