from os import path

from cffi import FFI

__clib_dir = path.join(path.dirname(__file__), 'libfab')

ffi = FFI()

with open(path.join(__clib_dir, 'include/fab.h')) as header:
    decls = []
    for line in header.readlines():
        if not line.startswith('#'):
            decls.append(line)
    ffi.cdef('\n'.join(decls))

with open(path.join(__clib_dir, "src/fab.c")) as cfile:
    lib = ffi.verify(cfile.read(), include_dirs=[path.join(__clib_dir, 'include')])
