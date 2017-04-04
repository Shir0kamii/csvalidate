# CSVALIDATE

Read or write CSV with validation

---

## Simple design

 * Use marshmallow to validate lines
 * Read or write a CSV as if it was a `DictReader` or `DictWriter`
 * Validate data with a schema
 * If data is not valid, a `ValidationError` exception is raised

---

## Simple usage

How to create a reader that validate data ?

<span class="fragment" data-fragment-access="1">**Simple**</span>

<span class="fragment" data-fragment-access="1">give your validation schema to `ValidatedReader.from_schema` !</span>

+++

```Python
from csvalidate import ValidatedReader
from marshmallow import Schema


class MySchema(Schema):
	# My validation schema
	pass

my_reader = ValidatedReader.from_schema(MySchema())
```

---

## Concrete example

I have a file with "id" and "name" column and I know that the "id" will be
integers.

How to validate data of this file ?

+++

```Python
from csvalidate import ValidatedReader
from marshmallow import Schema
from marshmallow.fields import Integer, String


class MySchema(Schema):
	id = Integer()
	name = String()

my_reader = ValidatedReader.from_schema(MySchema())
```
<span class="fragment">
`my_reader` can now be used as a `DictReader` except that it will raise
`ValidationError` exceptions when it reads an invalid line.
</span>

---

### Live Demo

(AKA fail time)

---

### Questions ?
