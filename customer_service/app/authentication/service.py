from datetime import datetime
from email import message
from flask import current_app, jsonify
from flask_jwt_extended import create_access_token

from app import db
from app.utils import message,err_resp, internal_err_resp
from app.models.user import User
from app.models.serializers import UserSchema

user_schema = UserSchema()


class AuthenticationService:
    @staticmethod
    def login(data:dict):
        """
            This method handles the login operation
        """
        email = data.get('email')
        password = data.get('password')
        try:
            if not (user := User.query.filter_by(email=email).first()):
                pass
                return err_resp('Email herhangi bir hesapla uyuşmadı',"email_404",404)
            elif user and user.verify_password(password):
                user_info = user_schema.dump(user)
                access_token = create_access_token(identity=user_info)
                resp = message('True', 'Login successful!')
                resp['access_token'] = access_token
                resp['user'] = user_info
                return resp,200
            return err_resp('Wrong email or password',"email_password_404",404)

        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()


    @staticmethod
    def register(data:dict):
        """
            This method handles the register operation
        """
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')
        is_owner = data.get('is_owner',False)

        if User.query.filter_by(email=email).first():
            return err_resp('This email is already exits.',"email_409",409)

        try:

            user = User(email=email,
                            first_name=first_name,
                            last_name=last_name,
                            joined_date=datetime.utcnow(),
                            is_owner=is_owner)
            user.set_password(password)
            #DB
            db.session.add(user)
            db.session.commit()

            user_info = user_schema.dump(user) # Convert JSON format the user model

            access_token = create_access_token(identity=user_info)
            res = message('True', 'Registration Successful!')
            res['access_token'] = access_token
            res['user'] = user_info
            return res,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
