from datetime import datetime
from app import db, bcrypt

# Alias common for  DB names
Column = db.Column
Model = db.Model
relationship = db.relationship


class Restaurant(Model):
    """ User model for storing user related data """

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(64), unique=True, index=True)
    products = db.relationship("Product", backref="restaurant", lazy="dynamic")
    joined_date = Column(db.DateTime, default=datetime.utcnow)
    owner = Column(db.Integer,nullable=False)


    def __repr__(self):
        return f"<Restaurant {self.id} {self.name}>"
