from flask import request
from flask_restx import Resource
from app.utils import validation_error
from flask_jwt_extended import jwt_required, get_jwt_identity,decode_token

from .data_manager import RestaurantManager
from .utils import RegisterRestaurantSchema, RegisterProductSchema
from .service import RestaurantService, ProductService

api = RestaurantManager.api
auth_success = RestaurantManager.auth_success


restaurant_register_schema = RegisterRestaurantSchema()
product_register_schema = RegisterProductSchema()


@api.route("/")
class RestaurantAPI(Resource):

    """Restaurant Register Endpoint"""

    restaurant_register = RestaurantManager.restaurant_register
    @api.doc("User Login",
        responses = {
            200: "Success",
            400: "Validation Error",
            401: "Forbidden"
            })
    @api.expect(restaurant_register,validate=True) #We tell to endpoint how data comes
    @jwt_required('headers')
    def post(self):
        restaurant_data = request.get_json()
        user = get_jwt_identity()


        if (errors := restaurant_register_schema.validate(restaurant_data)):
            return validation_error(False,errors),400

        return RestaurantService.register(restaurant_data,user)

@api.route("/<int:restaurant_id>/products")
class RestaurantProducts(Resource):
    @api.doc("Get all datasets of a specific user",responses={200:"Success",500:"Internal Server Error"})

    def get(self,restaurant_id):
        """Get all datasets of a specific user"""

        return RestaurantService.get_products(restaurant_id)

@api.route("/product")
class ProductAPI(Resource):
    """Product Register Endpoint"""



    product_register = RestaurantManager.product_register
    @api.expect(product_register,validate=True) #We tell to endpoint how data comes
    @jwt_required("headers")
    def post(self):

        product_data = request.get_json()
        user = get_jwt_identity()
        if (errors := product_register_schema.validate(product_data)):
            return validation_error(False,errors),400




        return ProductService.register(product_data,user)


"""@api.route("/register")
class UserRegisterAPI(Resource):

    User Register Endpoint

    auth_register = AuthenticationManager.auth_register
    @api.doc("User Register",
        responses = {
            200: "Success",
            400: "Validation Error",
            409: "Email already exist"})
    @api.expect(auth_register) #We tell to endpoint how data comes
    def post(self):

        user_register_data = request.get_json()

        print(user_register_data)
        # Validate register data
        if (errors := register_schema.validate(user_register_data)):
            return validation_error(False,errors),400

        return AuthenticationService.register(user_register_data)"""
