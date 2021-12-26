from marshmallow import fields, Schema
from project.schemas.movie import MovieSchema


class FavoriteMovieSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    movie = fields.Nested(MovieSchema)
