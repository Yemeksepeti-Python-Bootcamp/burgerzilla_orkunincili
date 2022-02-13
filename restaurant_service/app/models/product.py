from datetime import datetime
from app import db, bcrypt

# Alias common for  DB names
Column = db.Column
Model = db.Model
relationship = db.relationship


class Product(Model):
    """ User model for storing user related data """

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(64), unique=True, index=True)
    price = Column(db.Float)
    description = Column(db.Text)
    image_url = Column(db.String(128))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))


    def __repr__(self):
        return f"<Product {self.id} {self.name} {self.price}>"
