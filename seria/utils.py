def str_to_num(i, exact_match=True):
    """
    Attempts to convert a str to either an int or float
    """
    # TODO: Cleanup -- this is really ugly
    if not isinstance(i, str):
        return i
    try:
        _ = int(i)
        if not exact_match:
            return _
        elif str(_) == i:
            return _
        else:
            pass
    except ValueError:
        pass
    try:
        _ = float(i)
        if not exact_match:
            return _
        elif str(_) == i:
            return _
        else:
            pass
    except ValueError:
        pass
    return i


def set_defaults(kwargs, defaults):
    for k, v in defaults.items():
        if k not in kwargs:
            kwargs[k] = v
