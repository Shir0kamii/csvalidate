from csv import DictWriter

from marshmallow.exceptions import ValidationError


class ValidatedWriter(DictWriter):
    schema = None

    def __init__(self, f, fieldnames=None, *args, **kwargs):
        if fieldnames is None and self.schema is not None:
            fieldnames = list(self.schema._declared_fields)
        DictWriter.__init__(self, f, fieldnames, *args, **kwargs)

    def writerow(self, rowdict):
        if self.schema:
            data, errors = self.schema.dump(rowdict)
            if errors:
                if any(k != v for k, v in rowdict.items()):
                    raise ValidationError(errors, data=data)
            else:
                rowdict = data
        return DictWriter.writerow(self, rowdict)

    def writeheader(self):
        header = dict(zip(self.fieldnames, self.fieldnames))
        DictWriter.writerow(self, header)

    @classmethod
    def from_schema(cls, schema, name=None):
        return type(
            name if name is not None else "Writer",
            (cls, object),
            {"schema": schema}
        )
