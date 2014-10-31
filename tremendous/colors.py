from functools import partial

from tremendous.api import apply_format
from tremendous.bindings import lib as __lib

colors_16 = dict(
    bold=__lib.BOLD,
    italic=__lib.ITALIC,
    under=__lib.UNDER,
    under2=__lib.UNDER2,
    strike=__lib.STRIKE,
    blink=__lib.BLINK,
    flip=__lib.FLIP,
    black=__lib.BLACK,
    red=__lib.RED,
    green=__lib.GREEN,
    yellow=__lib.YELLOW,
    blue=__lib.BLUE,
    magenta=__lib.MAGENTA,
    cyan=__lib.CYAN,
    white=__lib.WHITE,
    hblack=__lib.HBLACK,
    hred=__lib.HRED,
    hgreen=__lib.HGREEN,
    hyellow=__lib.HYELLOW,
    hblue=__lib.HBLUE,
    hmagenta=__lib.HMAGENTA,
    hcyan=__lib.HCYAN,
    hwhite=__lib.HWHITE,
    bgblack=__lib.BGBLACK,
    bgred=__lib.BGRED,
    bggreen=__lib.BGGREEN,
    bgyellow=__lib.BGYELLOW,
    bgblue=__lib.BGBLUE,
    bgmagenta=__lib.BGMAGENTA,
    bgcyan=__lib.BGCYAN,
    bgwhite=__lib.BGWHITE,
)

__funcs = {}
# This is also gross. Sorry.
for k, v in colors_16.items():
    if k.startswith('h'):
        __funcs['highlight_' + k[1:]] = partial(apply_format, v)
        __funcs['hi_' + k[1:]] = partial(apply_format, v)
        __funcs['hl_' + k[1:]] = partial(apply_format, v)
    elif k.startswith('bg'):
        __funcs['background_' + k[1:]] = partial(apply_format, v)
        __funcs['bg_' + k[2:]] = partial(apply_format, v)
    elif k.startswith('under'):
        __funcs[k] = partial(apply_format, v)
        __funcs['underline' + k[5:]] = partial(apply_format, v)
    else:
        __funcs[k] = partial(apply_format, v)
