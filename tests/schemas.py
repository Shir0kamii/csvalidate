from marshmallow import Schema
from marshmallow.fields import Int, String


class TableIdName(Schema):
    id = Int()
    name = String()
