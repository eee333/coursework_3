from sqlalchemy.exc import IntegrityError

from project.config import DevelopmentConfig
from project.dao.models import Genre
from project.dao.models import Director
from project.server import create_app
from project.setup_db import db
from project.utils import read_json

app = create_app(DevelopmentConfig)

data = read_json("fixtures.json")

with app.app_context():
    for genre in data["genres"]:
        db.session.add(Genre(id=genre["pk"], name=genre["name"]))
    for director in data["directors"]:
        db.session.add(Director(id=director["pk"], name=director["name"]))

    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")
