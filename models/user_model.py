import sqlite3
from db import db


class UserModel(db.Model):
    # SQLAlchemy model setup
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # MUST be self.id else it will not work with flask_JWT idenity function
        # removed ID as implemented by SQLAlchemy
        # property names must match model names in order to be saved in db
        # not all properties have to be saved to db
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

        connection.close()
        return user