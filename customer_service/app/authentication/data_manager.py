from flask_restx import Namespace, fields

class AuthenticationManager:
    api = Namespace('auth', description='Authentication operations')


    user_obj = api.model('User Object', {
        "email": fields.String,
        "first_name": fields.String,
        "last_name": fields.String,
        "joined_date": fields.DateTime,
        "is_owner": fields.Boolean
    })

    auth_login = api.model('Login Data', {
        "email": fields.String(required=True, description="User email address"),
        "password": fields.String(required=True, description="User password")
    })

    auth_register = api.model('Register Data',
    {   "email": fields.String(required=True, description="User email address"),
        "first_name": fields.String(required=True, description="User first name"),
        "last_name": fields.String(required=True, description="User last name"),
        "password": fields.String(required=True, description="User password"),
        "is_owner": fields.Boolean(required=False, description="Is user owner?")
    })

    auth_success = api.model('Auth Success Response',
    {
     "message": fields.String,
     "access_token": fields.String,
     "user": fields.Nested(user_obj)
    })
