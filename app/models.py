from . import db



class Users(db.Model):
    ''' Users create a user model'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
