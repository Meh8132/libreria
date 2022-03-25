from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    password = db.Column(db.String(40))
    address = db.Column(db.String(80))