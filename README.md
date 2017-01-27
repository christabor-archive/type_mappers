*This project is incomplete and undergoing major change. It is currently unstable and thus not meant for production use.*

# Type Mapper

A utility to map primitive types (int, str, bool, etc) to the equivalent in various python libraries.

## What?

It's really simple easy: using a 'string' representation, this utility maps commonly named types into their actual programmatic equivalent. An example will help:

given `'str'` and `'boolean'`, we know intuitively that these will always map to `str` and `bool` in python, respectively.

But that's just the simple stuff. There are many more types that don't have an exact equivalent in python (`double`, `long`, etc..., which map to `float` in this case), so we use the most obvious approximation. These are very predictable, so you'll get what you expect.

When it comes to building classes or other functionality *dynamically*, there are often times when primitive types are involved.

This is especially true for code generation.

Many scenarios where some collection of types need to map to another similar collection, but more specific: an int to a sqlalchemy field, wtform field, or something else entirely. This is such a fundamental thing to do that it seems that a library ought to exist for many of these scenarios.

## Goals

* Be dead simple to use
* Extremely lighweight
* Have a very comprehensive set of unique mappings
* Have a very comprehensive set of synonymous mappings (str, string, text, word, etc... all really mean the same thing.)

## Contexts

Currently the following exist:

* Vanilla (native python)
* SqlAlchemy
* WTForms
* Factory Boy

Want to see new ones? File an issue!

## Built on these simple rules:

* The mapping key is always a string representation so it can be stored in a dictionary and not be confused with another type.
* All mappings TO a type must be callable. You will always get back a callable type.

## Future ideas for types/support

### HTML5 types

* color
* email

### GIS/Geospatial

* coordinates
* geojson

## Tests

Tests mainly ensure that there is parity across each context. To run, assuming you are in a virtualenv and have run `pip install -e .`, then run `pytest tests`.
