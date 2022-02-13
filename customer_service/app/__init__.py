"""
APP initializer
"""
from flask import Flask
from .extensions import bcrypt, cors, db, jwt, ma
from config import config_by_name
from .authentication import auth_blueprint

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    register_extensions(app)




    app.register_blueprint(auth_blueprint)

    #from .api import api_bp

    #app.register_blueprint(api_bp, url_prefix="/api")

    return app


def register_extensions(app):
    # Registers flask extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
