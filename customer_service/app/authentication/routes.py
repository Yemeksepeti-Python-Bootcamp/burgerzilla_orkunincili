from flask import request
from flask_restx import Resource
from app.utils import validation_error


from .data_manager import AuthenticationManager
from .utils import LoginSchema,RegisterSchema
from .service import AuthenticationService

api = AuthenticationManager.api
auth_success = AuthenticationManager.auth_success

login_schema = LoginSchema()
register_schema = RegisterSchema()



@api.route("/login")
class UserLoginAPI(Resource):

    """User Login Endpoint"""

    auth_login = AuthenticationManager.auth_login
    @api.doc("User Login",
        responses = {
            200: "Success",
            400: "Validation Error",
            403: "Invalid Credentials",
            404: "User Not Found"})
    @api.expect(auth_login,validate=True) #We tell to endpoint how data comes
    def post(self):

        user_login_data = request.get_json()
        if (errors := login_schema.validate(user_login_data)):
            return validation_error(False,errors),400

        return AuthenticationService.login(user_login_data)


@api.route("/register")
class UserRegisterAPI(Resource):

    """User Register Endpoint"""

    auth_register = AuthenticationManager.auth_register
    @api.doc("User Register",
        responses = {
            200: "Success",
            400: "Validation Error",
            409: "Email already exist"})
    @api.expect(auth_register) #We tell to endpoint how data comes
    def post(self):

        user_register_data = request.get_json()

        
        # Validate register data
        if (errors := register_schema.validate(user_register_data)):
            return validation_error(False,errors),400

        return AuthenticationService.register(user_register_data)
