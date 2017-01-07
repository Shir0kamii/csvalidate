from csv import DictReader
import os

import pytest

from csvalidate import ValidatedReader

SAMPLE_FILENAME = "files/sample.csv"


@pytest.fixture
def original(request):
    with open(os.path.join(os.path.dirname(__file__), SAMPLE_FILENAME)) as fp:
        yield DictReader(fp)


@pytest.fixture
def validated(request):
    with open(os.path.join(os.path.dirname(__file__), SAMPLE_FILENAME)) as fp:
        yield ValidatedReader(fp)


def test_compatible_ReadDict(original, validated):
    for original_obj, validated_obj in zip(original, validated):
        assert original_obj == validated_obj
