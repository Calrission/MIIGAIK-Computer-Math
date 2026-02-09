from math import pi


def math_input(text: str, default=None, converter=int):
    value = input(text)
    if value == "" and default is not None:
        res = default
    elif value == "PI":
        res = pi
    else:
        res = converter(value)
    return res

