# -*- coding: utf-8 -*-

from .serializers import Serializer


def load(stream, *args, **kwargs):
    return Serializer(stream, *args, **kwargs)