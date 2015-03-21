# -*- coding: utf-8 -*-
from string import printable

def str_to_num(data):
    """ Attempts to convert a str to either an int or float """
    for structure in [int, float]:
        if isinstance(data, structure):
            return data
    try:
        data = float(data)
    except ValueError as error:
        data = float(str(error).strip(printable[10:]))
    if data.is_integer():
        data = int(data)
    return data

def set_defaults(kwargs, defaults):
    for key, value in defaults.items():
        if key not in kwargs:
            kwargs[key] = value
