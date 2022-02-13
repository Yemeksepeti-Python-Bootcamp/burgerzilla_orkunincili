from flask_restx import Api
from flask import Blueprint
from .routes import api as auth_namespace


auth_blueprint = Blueprint('auth', __name__)

auth = Api(auth_blueprint, title='Authentication App', version='1.0')

auth.add_namespace(auth_namespace)
