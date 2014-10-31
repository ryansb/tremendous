from tremendous.bindings import lib
from tremendous.bindings import ffi

def apply_format(color, body):
    s = lib.apply_format(color, body)
    return ffi.string(s)
