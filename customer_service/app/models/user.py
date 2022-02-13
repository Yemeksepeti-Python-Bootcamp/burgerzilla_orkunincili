from datetime import datetime
from app import db, bcrypt

# Alias common for  DB names
Column = db.Column
Model = db.Model
relationship = db.relationship

class User(Model):
    """ User model for storing user related data """

    id = Column(db.Integer, primary_key=True)
    email = Column(db.String(64), unique=True, index=True)
    first_name = Column(db.String(15))
    last_name = Column(db.String(64))
    password_hash = Column(db.String(128))
    joined_date = Column(db.DateTime, default=datetime.utcnow)
    is_owner = Column(db.Boolean,default=False)


    def __repr__(self):
        return f"<User {self.id} {self.first_name} {self.last_name}>"

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
