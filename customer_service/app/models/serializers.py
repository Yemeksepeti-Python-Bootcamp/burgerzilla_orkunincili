from app import ma
from .user import User

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","email", "first_name", "last_name", "joined_date", "is_owner")
