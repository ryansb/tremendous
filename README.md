# tremendous

Powered by [libfab](https://github.com/rossdylan/libfab)

`tremendous` is a Python wrapper around `libfab`, a C library that acts like
fabulous. It makes dealing with terminal coloring easy for standard 16-color
terminals and extended 256-color environments.

```
from tremendous import green, red, bold

# every color is a function that wraps a string with terminal escape codes
print green("Hello, and welcome to computers")

# colors, backgrounds, and modifiers can be stacked
print bold(red("Bad things happened!"))

# 256 colors are available from tremendous.ext
from tremendous.ext import darkgreen
print darkgreen("Crisis averted"))
```
