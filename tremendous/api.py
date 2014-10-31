from tremendous.bindings import lib
from tremendous.bindings import ffi

def apply_format(color, body):
    s = lib.apply_format(color, body)
    return ffi.string(s)

def apply_formats(colors, body):
    if isinstance(colors, int):
        colors = [colors]

    for c in colors:
        body = apply_format(c, body)

    return body
