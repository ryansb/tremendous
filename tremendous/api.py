from tremendous.bindings import lib
from tremendous.bindings import ffi


def apply_format(color, body):
    try:
        s = lib.apply_format(color, body)
        return ffi.string(s)
    except:
        s = lib.apply_format(color, bytes(body, 'utf-8'))
        return ffi.string(s).decode('utf-8')


def apply_256(rgb_t, body):
    try:
        s = lib.foreground_256(rgb_t, body)
        return ffi.string(s)
    except:
        s = lib.foreground_256(rgb_t, bytes(body, 'utf-8'))
        return ffi.string(s).decode('utf-8')


def apply_256_bg(rgb_t, body):
    try:
        s = lib.background_256(rgb_t, body)
        return ffi.string(s)
    except:
        s = lib.background_256(rgb_t, bytes(body, 'utf-8'))
        return ffi.string(s).decode('utf-8')


def apply_256_hl(rgb_t, body):
    try:
        s = lib.highlight_256(rgb_t, body)
        return ffi.string(s)
    except:
        s = lib.highlight_256(rgb_t, bytes(body, 'utf-8'))
        return ffi.string(s).decode('utf-8')
