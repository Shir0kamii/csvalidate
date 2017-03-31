from marshmallow import Schema
from marshmallow.fields import Int, String


class TableIdName(Schema):
    class Meta(object):
        ordered = True
    id = Int()
    name = String()
