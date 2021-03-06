from marshmallow import fields, Schema


class UserSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    role = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre_id = fields.Int()
