#!flask/bin/python
from config import SQLALCHEMY_DATABASE_URI
from Ostrich import db
db.create_all()