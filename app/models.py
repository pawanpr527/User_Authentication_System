#models.py
from app import db
from flask_login import UserMixin
# Flask-Login jab check karega ki koi user login hai ya nahi, ya kis id se login hai, to UserMixin un sabka jawab de dega automatically.

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(200),nullable=False,unique=True)
    email = db.Column(db.String(200),nullable=False,unique=True)
    password = db.Column(db.String(200),nullable=False)
    is_verified = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"{self.username} , {self.email}"


