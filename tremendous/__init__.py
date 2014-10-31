from cffi import FFI

ffi = FFI()

with open('./libfab/include/fab.h') as header:
    decls = []
    for line in header.readlines():
        if not line.startswith('#'):
            decls.append(line)
    ffi.cdef('\n'.join(decls))

_lib = ffi.verify(open("./libfab/src/fab.c").read(), include_dirs=["./libfab/include"])
