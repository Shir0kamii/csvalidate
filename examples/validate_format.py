from marshmallow import Schema
from marshmallow.fields import Integer, String

from csvalidate import ValidatedReader


class IdName(Schema):
    id = Integer()
    name = String()


class TableReader(ValidatedReader):
    schema = IdName()


f = open("/tmp/unsure_about_validity.csv")
reader = TableReader(f)
try:
    list(reader)
    print("Valid id/name table")
except:
    print("Invalid id/name table")
f.close()
