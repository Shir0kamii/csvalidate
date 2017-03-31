from pymongo import MongoClient
from marshmallow import Schema
from marshmallow.fields import Integer, String

from csvalidate import ValidatedWriter


collection = MongoClient("mongodb://localhost").test.test


class IdName(Schema):
    id = Integer()
    name = String()


class CollectionDumper(ValidatedWriter):
    schema = IdName()


f = open("/tmp/mongo_dump.csv", 'w')
dumper = CollectionDumper(f)
dumper.writeheader()
for doc in collection.find():
    dumper.writerow(doc)
f.close()
