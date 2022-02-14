from datetime import datetime
from app import db, bcrypt
import enum
# Alias common for  DB names
Column = db.Column
Model = db.Model
relationship = db.relationship

class OrderStatus(enum.Enum):
    now = 0
    preparing = 1
    on_the_way = 2
    done = 3
    cancel = 4

class Order(Model):
    """ Order model for storing user related data
        NOTE: Status logic is not ready!!!
    """

    id = Column(db.Integer, primary_key=True)
    product_id = Column(db.Integer,nullable=False)
    user_id = Column(db.Integer,nullable=False)
    created_at = Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Enum(OrderStatus))


    def __repr__(self):
        return f"<Order id:{self.id} product_id:{self.product_id} user_id:{self.user_id}>"
