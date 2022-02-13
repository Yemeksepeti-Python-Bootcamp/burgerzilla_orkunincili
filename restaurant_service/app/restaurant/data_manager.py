from flask_restx import Namespace, fields

class RestaurantManager:
    api = Namespace('restaurant', description='Restaurant operations')


    restaurant_obj = api.model('User Object', {
        "name": fields.String,
        "joined_date": fields.DateTime,
        "is_owner": fields.Integer
    })



    restaurant_register = api.model('Register Data',
    {
        "name": fields.String(required=True, description="Restaurant name")
    })

    product_register = api.model("Product Data",
    {
        "name": fields.String(required=True, description="Product name"),
        "price": fields.Float(required=True, description="Product price"),
        "description": fields.String(required=True,description="Product description"),
        "image_url": fields.String(required=True,description="Product image url")

    })

    auth_success = api.model('Restaurant Success Response',
    {
     "message": fields.String,
     "user": fields.Nested(restaurant_obj)
    })
