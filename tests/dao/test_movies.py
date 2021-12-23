import pytest

from project.dao import MovieDAO
from project.dao.models import Movie


class TestMovieDAO:
    @pytest.fixture(autouse=True)
    def dao(self, db):
        self.dao = MovieDAO(db.session)

    @pytest.fixture
    def movie_1(self, db):
        m = Movie(
            title="Йеллоустоун",
            description="Владелец ранчо",
            trailer="https://www.youtube.com/watch?v=UKei_d0cbP4",
            year=2018,
            rating=8.6,
            genre_id=17,
            director_id=1
        )
        db.session.add(m)
        db.session.commit()
        return m

    @pytest.fixture
    def movie_2(self, db):
        m = Movie(
            title="Омерзительная восьмерка",
            description="США после Гражданской",
            trailer="https://www.youtube.com/watch?v=lmB9VWm0okU",
            year=2015,
            rating=7.8,
            genre_id=4,
            director_id=2
        )
        db.session.add(m)
        db.session.commit()
        return m

    def test_get_movie_by_id(self, movie_1):
        assert self.dao.get_by_id(movie_1.id) == movie_1

    def test_get_movie_by_id_not_found(self):
        assert self.dao.get_by_id(1) is None

    def test_get_all_movies(self, movie_1, movie_2):
        assert self.dao.get_all() == [movie_1, movie_2]
