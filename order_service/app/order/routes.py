from flask import request
from flask_restx import Resource
from app.utils import validation_error
from flask_jwt_extended import jwt_required, get_jwt_identity,decode_token

from .data_manager import OrderManager
from .utils import OrderCreateSchema
#from .service import RestaurantService, ProductService

api = OrderManager.api
order_create = OrderCreateSchema()
