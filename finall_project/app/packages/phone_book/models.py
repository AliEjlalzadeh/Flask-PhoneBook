from app.init import db


class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), )
    family = db.Column(db.String(), )
    phone_number = db.Column(db.String(), unique=True)
