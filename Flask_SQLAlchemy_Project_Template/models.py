from .database import db


class Users(db.Model):    # name of table, flask will translate the Name to lowercase "users"
    # class attributes, not instance attributes
    # if using multiple threads to create user, I guess attributes will be easily overwritten and make a mess here
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    profile = db.Column(db.String, unique=False, nullable=False)


class InternalUse(db.Model):     # name of table, flask will translate CamelCase to snake_case "internal_use"
    id = db.Column(db.Integer, primary_key=True)
    browser_open = db.Column(db.Integer, unique=False, nullable=True)
    statistics = db.Column(db.String, unique=False, nullable=True)
    commercials = db.Column(db.String, unique=False, nullable=True)
