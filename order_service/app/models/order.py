from datetime import datetime
from app import db, bcrypt

# Alias common for  DB names
Column = db.Column
Model = db.Model
relationship = db.relationship


class Order(Model):
    """ Order model for storing user related data """

    id = Column(db.Integer, primary_key=True)
    product_id = Column(db.Integer,nullable=False)
    user_id = Column(db.Integer,nullable=False)
    created_at = Column(db.DateTime, default=datetime.utcnow)



    def __repr__(self):
        return f"<Order id:{self.id} product_id:{self.product_id} user_id:{self.user_id}>"
