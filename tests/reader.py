from csv import DictReader
import os

import pytest

from csvalidate import ValidatedReader


class ReaderFixture(object):

    def __init__(self, reader, filename):
        self.filename = filename
        self.reader = reader

    def __enter__(self):
        cur_dir = os.path.dirname(__file__)
        self.file = open(os.path.join(cur_dir, self.filename))
        return self.reader(self.file)

    def __exit__(self, *excinfo):
        self.file.close()


def original(filename):
    return ReaderFixture(DictReader, filename)


def validated(filename):
    return ReaderFixture(ValidatedReader, filename)


@pytest.fixture(params=["files/sample.csv", "files/table_id_name.csv"])
def readers(request):
    filename = request.param
    with validated(filename) as _validated:
        with original(filename) as _original:
            yield _original, _validated


def test_compatible_ReadDict(readers):
    original, validated = readers
    print(original, validated)
    for original_obj, validated_obj in zip(*readers):
        assert original_obj == validated_obj
