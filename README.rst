##########
csvalidate
##########

csvalidate is a minimal library for reading from and writing to csv with an
added layer of validation

Get Started
###########

Installation
============

As any python package, you can install it via pip::

    $ pip install csvalidate

How ot use it ?
===============

The gist of it is to subclass one of `ValidatedReader` or `ValidatedWriter` and
add a `schema` class attribute that defines validation.

Examples can be found in the `examples` directory.
