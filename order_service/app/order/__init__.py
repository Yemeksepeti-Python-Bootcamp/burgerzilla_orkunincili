from flask_restx import Api
from flask import Blueprint
from .routes import api as order_namespace


order_blueprint = Blueprint('order', __name__)

order = Api(order_blueprint, title='Order App', version='1.0')

order.add_namespace(order_namespace)
