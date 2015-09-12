from flask.ext.sqlalchemy import SQLAlchemy
from Ostrich import app
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    location = db.Column(db.String(100), unique=False)
    course = db.Column(db.String(15), unique=False)
    shirt = db.Column(db.String(100), unique=False)

    def __init__(self, name, location, course, shirt):
        self.name = name
        self.location = location
        self.course = course
        self.shirt = shirt

    def __repr__(self):
        return '<User %r>' % self.name

db.drop_all()
db.create_all()
