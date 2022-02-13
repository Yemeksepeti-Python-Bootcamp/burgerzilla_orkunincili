from datetime import datetime
from app import db, bcrypt

# Alias common for  DB names
Column = db.Column
Model = db.Model
relationship = db.relationship


class Menu(Model):
    """ Restaurant model for storing user related data """

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(64), unique=True, index=True)
    created_date = Column(db.DateTime, default=datetime.utcnow)
    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))


    def __repr__(self):
        return f"<Menu {self.id} {self.name}>"
