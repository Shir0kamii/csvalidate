##########
csvalidate
##########

csvalidate is a minimal library for reading from and writing to csv with an
added layer of validation

Status
######

Even though csvalidate doesn't get much work, it is maintained. Don't hesitate
to open issues or pull requests.

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
