from flask_restx import Api
from flask import Blueprint
from .routes import api as restaurant_namespace


restaurant_blueprint = Blueprint('restaurant', __name__)

restaurant = Api(restaurant_blueprint, title='Restaurant App', version='1.0')

restaurant.add_namespace(restaurant_namespace)
