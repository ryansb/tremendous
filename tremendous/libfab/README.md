libfab
======

A port of the python library fabulous to C

The python library [fabulous](https://github.com/jart/fabulous) is as the name implies, fabulous.
however it hasn't seen an update in a while. libfab is a port of the core functionality of fabulous to C.
Once it is ported wrappers to other languages can be made. I'm working on this to improve my knowledge of C,
and to improve upon a library I enjoy using.

Dependencies
============

* ImageMagick

Building
========

You can use either `make` or [tup](https://github.com/gittup/tup) to build
libfab.

To use tup, clone it `git clone https://github.com/gittup/tup` and use
their `bootstrap.sh` script to build the tup binary.

Once tup is built, you need to run `tup init` the first time, then all
subsequent builds you can use `tup upd` or just `tup` to rebuild libfab and its
libraries.

Porting Status
==============
- [x] Text Formatting
- [x] Basic Text Coloring
- [x] 256color text Coloring
- [ ] Color Complements
- [ ] Advanced Color specification
- [x] Images -> ASCII

Attribution
============
The original [Fabulous](https://github.com/jart/fabulous) was a huge inspiration, and the existing code was a huge help in writing libfab

The xterm, RGB conversion code, the algorithm for rendering images in the
terminal, and the rest of fabulous were created by [Justine Tunney](https://github.com/jart/).
