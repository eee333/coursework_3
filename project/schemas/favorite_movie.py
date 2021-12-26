from marshmallow import fields, Schema


class FavoriteMovieSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    movie_id = fields.Int(required=True)
