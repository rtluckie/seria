# -*- coding: utf-8 -*-

from .serializers import Serializer

def seria(stream, *args, **kwargs):
    return Serializer(stream, *args, **kwargs)