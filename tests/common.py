from .schemas import TableIdName

file_schemas = [
    ("files/sample.csv", None),
    ("files/table_id_name.csv", TableIdName)
]

files = [line[0] for line in file_schemas]
