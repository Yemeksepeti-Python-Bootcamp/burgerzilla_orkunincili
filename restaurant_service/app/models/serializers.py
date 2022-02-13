from app import ma
from .restaurant import Restaurant
from .menu import Menu
from .product import Product

class RestaurantSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("name", "joined_date", "owner")


class MenuSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("name", "created_date","restaurant_id")


class ProductSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("name", "price", "description", "image_url", "restaurant_id")
