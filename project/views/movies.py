from flask_restx import abort, Namespace, Resource, reqparse

from project.exceptions import ItemNotFound
from project.services import MoviesService
from project.setup_db import db

movies_ns = Namespace("movies")
parser = reqparse.RequestParser()
parser.add_argument('page', type=int)


@movies_ns.route("/")
class MoviesView(Resource):
    @movies_ns.expect(parser)
    @movies_ns.response(200, "OK")
    def get(self):
        """Get all movies"""
        page = parser.parse_args().get("page")
        if page:
            return MoviesService(db.session).get_limit_movies(page)
        else:
            return MoviesService(db.session).get_all_movies()


@movies_ns.route("/<int:movie_id>")
class MovieView(Resource):
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def get(self, movie_id: int):
        """Get movie by id"""
        try:
            return MoviesService(db.session).get_item_by_id(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")
