from flask import request
from flask_restx import Resource
from app.utils import validation_error
from flask_jwt_extended import jwt_required, get_jwt_identity,decode_token

from .data_manager import OrderManager
from .utils import OrderCreateSchema
from .service import OrderService

from app.models.order import Order

api = OrderManager.api
order_create = OrderCreateSchema()



@api.route("/")
class OrderList(Resource):

    @jwt_required('headers')
    def get(self):
        """
            get all orders from id
        """
        user = get_jwt_identity()
        #Normally, owner user may be make order in the future but in this conditions user is owner(restaurant) or not
        is_owner = user.get("is_owner")

        user_id = user.get("id")


        if is_owner:
          """
                ### NOT READY
                make get request with user id if the user is owner and fetch restaurant info
                from restaurant service(port 5001)

                The idea;

                res = request.get(http://localhost:5001/restaurant/<int:owner_id>)
                data = res.json()
                restaurant_id = data['restaurant_id']

            """
            orders = Order.query.filter_by(restaurant_id=restaurant_id)

            return orders #convert json --- not ready

        else:

            orders = Order.query.filter_by(user_id=user_id)

            return orders #convert json --- not ready

@api.route("/<int:product_id>")
class OrderAPI(Resource):

    @api.expect(order_create,validate=True)
    @jwt_required('headers')
    def post(self):
        """
            Order create
        """
        order_data = request.get_json()
        user = get_jwt_identity()

        return OrderService.create_order(order_data,user)


@api.route("<int:product_id>/status")
class OrderStatusAPI(Resource):
    """
        Status logic is not ready! But here is my idea as basic!!!
    """
    @jwt_required('headers')
    def get(self):

        user = get_jwt_identity()
        user_id = user.get("id")
        order = Order.query.filter(product_id=product_id)

        if user_id != order.user_id:
            """Check if the user has accessed his own order"""
            return {"message":"You dont have permission"}

        else:
            return {"status":order.status}
