rom datetime import datetime
from email import message
from flask import current_app, jsonify

from app import db
from app.utils import message,err_resp, internal_err_resp
from app.models.order import Order

from app.models.serializers import OrderSchema

order_schema = OrderSchema()



class RestaurantService:



    @staticmethod
    def create_order(data:int,user:dict):
        """
            This method handles the create order operation
        """
        product_id = data.get('product_id')
        user_id = user.get("id")

        try:
            order = Order(product_id=product_id,created_at=datetime.utcnow(),user_id=user_id)
            #DB
            db.session.add(order)
            db.session.commit()
            order_info = restaurant_schema.dump(order) # Convert JSON format the user model

            res = message('True', 'Order Create Successful!')

            res['order'] = order_info
            return res,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
