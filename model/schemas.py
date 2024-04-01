
from marshmallow import Schema, fields, validate

class EmployeeSchema(Schema):
    name = fields.Str(required=True, validate=[
        validate.Length(max=100),
        validate.Regexp(r'^[a-zA-Z\s]*$', error='only characters are allowed in the name field.')
    ])
    salary = fields.Float(required=True, validate=validate.Range(min=0))
