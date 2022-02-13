from flask_restx import Namespace, fields

class OrderManager:
    api = Namespace('order', description='Order operations')


    restaurant_obj = api.model('User Object', {
        "id": fields.Integer,
        "user_id": fields.Integer,
        "product_id": fields.Integer,
        "created_at": fields.DateTime,

    })



    order_create = api.model('Register Data',
    {
        "user_id": fields.Integer(required=True),
        "product_id": fields.Integer(required=True)
    })
