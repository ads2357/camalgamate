# camalgamate
Combines C/C++ source files into a single compilable file or header

## What?

This tool scans a set of C/C++ source files, in particular the header files, which may #include each other.
It resolves these implied dependencies in order to produce a partial ordering in which no file is included before
the files it depends on. It can then output a concatenation which can act as a single header or a single standalone
.c file.

The difference between this and gcc -E is the fact that the latter would include system headers and expand macros.

## But why?

I wrote this tool in order to simplify coursework submission at university. It could also be used to merge header
files, if such a thing is ever desirable.
