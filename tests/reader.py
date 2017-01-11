from csv import DictReader
import os

import pytest
from marshmallow.exceptions import ValidationError

from csvalidate import ValidatedReader

from tests.common import file_schemas, files
from tests.schemas import TableIdName


class ReaderFixture(object):

    def __init__(self, reader, filename, schema=None):
        self.filename = filename
        self.reader = reader
        self.schema = schema

    def __enter__(self):
        cur_dir = os.path.dirname(__file__)
        self.file = open(os.path.join(cur_dir, self.filename))
        if self.schema:
            result = self.reader(self.file)
            result.schema = self.schema()
            return result
        return self.reader(self.file)

    def __exit__(self, *excinfo):
        self.file.close()


@pytest.fixture(params=files)
def readers(request):
    filename = request.param
    with ReaderFixture(ValidatedReader, filename) as _validated:
        with ReaderFixture(DictReader, filename) as _original:
            yield _original, _validated


@pytest.fixture(params=file_schemas, ids=files)
def validated_reader(request):
    filename, schema = request.param
    with ReaderFixture(ValidatedReader, filename, schema) as _validated:
        yield _validated


def test_compatible_ReadDict(readers):
    original, validated = readers
    for original_obj, validated_obj in zip(*readers):
        assert original_obj == validated_obj


def test_output_dict(validated_reader):
    for d in validated_reader:
        assert isinstance(d, dict)


def test_exception_bad_id():
    filename = "files/bad_id.csv"
    with ReaderFixture(ValidatedReader, filename, TableIdName) as reader:
        with pytest.raises(ValidationError):
            print(list(reader))
