from flask_sqlalchemy import flask_sqlalchemy

db= SQLAlchemy()

class pig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(30), index=True)
    name = db.Column(db.String(150, nullable=False))
    