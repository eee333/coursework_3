import pytest

from project.dao.models import Genre
from tests.views.auth_mock import AuthMock


class TestGenresView(AuthMock):
    url = "/genres/"

    @pytest.fixture
    def genre(self, db):
        g = Genre(name="Боевик")
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_genres(self, client, genre, auth_mock):
        response = client.get(self.url)
        assert response.status_code == 200
        assert response.json == [
            {"id": genre.id, "name": genre.name},
        ]


class TestGenreView(AuthMock):
    url = "/genres/{genre_id}"

    @pytest.fixture
    def genre(self, db):
        g = Genre(name="Боевик")
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_genre(self, client, genre, auth_mock):
        response = client.get(self.url.format(genre_id=genre.id))
        assert response.status_code == 200
        assert response.json == {"id": genre.id, "name": genre.name}

    def test_genre_not_found(self, client, auth_mock):
        response = client.get(self.url.format(genre_id=10))
        assert response.status_code == 404
