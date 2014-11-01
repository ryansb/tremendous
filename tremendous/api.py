from tremendous.bindings import lib
from tremendous.bindings import ffi


def apply_format(color, body):
    s = lib.apply_format(color, body)
    return ffi.string(s)


def apply_256(rgb_t, body):
    s = lib.foreground_256(rgb_t, body)
    return ffi.string(s)


def apply_256_bg(rgb_t, body):
    s = lib.background_256(rgb_t, body)
    return ffi.string(s)


def apply_256_hl(rgb_t, body):
    s = lib.highlight_256(rgb_t, body)
    return ffi.string(s)
