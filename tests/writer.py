import pytest

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
    with WriterFixture(ValidatedWriter, "/tmp/validated.txt",
                       TableIdName) as _validated:
        yield _validated


def test_compatible_DictWriter(writers):
    original, validated = writers
    d = {"id": 42, "name": "Life"}
    assert original.writerow(d) == validated.writerow(d)
    f1 = open("/tmp/original.txt")
    f2 = open("/tmp/validated.txt")
    assert f1.read() == f2.read()


def test_correct_output(validated_writer):
    d = {"id": 42, "name": "Life"}
    validated_writer.writerow(d)
    f1 = open("/tmp/original.txt")
    assert f1.read().strip() == "42,Life"


def test_exception_bad_id(validated_writer):
    with pytest.raises(ValueError):
        validated_writer.writerow({"id": "WHAT", "name": "Life"})


def test_can_infere_fieldnames():
    ValidatedWriter.schema = TableIdName
    f = open("/tmp/whatever", 'w')
    ValidatedWriter(f)  # Raise an exception if the test fail
    ValidatedWriter.schema = None


def test_from_schema():
    writer = ValidatedWriter.from_schema(TableIdName)
    assert writer.schema is TableIdName
