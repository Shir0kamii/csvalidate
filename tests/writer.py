import pytest
import os

from marshmallow.exceptions import ValidationError

from csvalidate.writer import DictWriter, ValidatedWriter

from .schemas import TableIdName


class WriterFixture(object):

    def __init__(self, writer, filename, schema=None):
        self.filename = filename
        self.writer = writer
        self.schema = schema

    def __enter__(self):
        self.file = open(self.filename, 'w')
        fieldnames = list(TableIdName._declared_fields)
        if self.schema:
            result = self.writer(self.file, fieldnames)
            result.schema = self.schema()
            return result
        return self.writer(self.file, fieldnames)

    def __exit__(self, *excinfo):
        self.file.close()


@pytest.fixture
def writers():
    with WriterFixture(ValidatedWriter, "/tmp/validated.txt") as _validated:
        with WriterFixture(DictWriter, "/tmp/original.txt") as _original:
            yield _original, _validated


@pytest.fixture
def validated_writer():
    with WriterFixture(ValidatedWriter, "/tmp/validated.txt", TableIdName) as _validated:
        yield _validated


def test_compatible_DictWriter(writers):
    original, validated = writers
    d = {"id": 42, "name": "Life"}
    assert original.writerow(d) == validated.writerow(d)
    f1 = open("/tmp/original.txt")
    f2 = open("/tmp/validated.txt")
    assert f1.read() == f2.read()


def test_output_bytes(validated_writer):
    d = {"id": 42, "name": "Life"}
    min_expected_length = sum(map(lambda v: len(str(v)), d.values()))
    assert validated_writer.writerow(d) >= min_expected_length


def test_exception_bad_id(validated_writer):
    with pytest.raises(ValidationError):
        validated_writer.writerow({"id": "WHAT", "name": "Life"})
