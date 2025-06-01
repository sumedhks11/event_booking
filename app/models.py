from . import db
class Event(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    date=db.Column(db.String(50))
    location=db.Column(db.String(100))
    description=db.Column(db.Text)