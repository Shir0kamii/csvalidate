from csv import DictReader

from marshmallow.exceptions import ValidationError


class ValidatedReader(DictReader):
    schema = None

    def __next__(self):
        obj = DictReader.__next__(self)
        if self.schema:
            data, errors = self.schema.load(obj)
            if errors:
                raise ValidationError(errors, data=data)
            obj = data
        return obj

    def next(self):
        if not hasattr(DictReader, "__next__"):
            DictReader.__next__ = DictReader.next
        return self.__next__()

    @classmethod
    def from_schema(cls, schema, name=None):
        return type(
            name if name is not None else "Reader",
            (cls, object),
            {"schema": schema}
        )
