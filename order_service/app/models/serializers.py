from app import ma
from .order import Order

class OrderSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","product_id","user_id","created_at")
