from csv import DictReader

from marshmallow.exceptions import ValidationError


class ValidatedReader(DictReader):
    schema = None

    def __next__(self):
        obj = super(ValidatedReader, self).__next__()
        if self.schema:
            data, errors = self.schema.load(obj)
            if errors:
                raise ValidationError(errors, data=data)
            obj = data
        return obj
