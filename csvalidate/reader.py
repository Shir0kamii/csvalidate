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
