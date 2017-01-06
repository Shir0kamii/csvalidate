def test_fields_in_package():
    try:
        from csvalidate import fields
    except ImportError:
        fields = None
    assert fields


def test_schema_in_package():
    try:
        from csvalidate import Schema
    except ImportError:
        Schema = None
    assert Schema
