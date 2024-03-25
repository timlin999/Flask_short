import datetime

from . import db


class URLmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True)
    short = db.Column(db.String(6), unique=True)
    visits = db.Column(db.Integer, default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
