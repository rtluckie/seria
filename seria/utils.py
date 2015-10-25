# -*- coding: utf-8 -*-

def str_to_num(i, exact_match=True):
    """
    Attempts to convert a str to either an int or float
    """
    # TODO: Cleanup -- this is really ugly
    if not isinstance(i, str):
        return i
    try:
        if not exact_match:
            return int(i)
        elif str(int(i)) == i:
            return int(i)
        elif str(float(i)) == i:
            return float(i)
        else:
            pass
    except ValueError:
        pass
    return i


def set_defaults(kwargs, defaults):
    for k, v in defaults.items():
        if k not in kwargs:
            kwargs[k] = v
