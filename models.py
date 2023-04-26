from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AnsanNewsReact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_src = db.Column(db.String, nullable=True, default=None)
    link = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False)
