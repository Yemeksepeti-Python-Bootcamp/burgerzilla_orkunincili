from datetime import datetime
from email import message
from flask import current_app, jsonify
from flask_jwt_extended import create_access_token

from app import db
from app.utils import message,err_resp, internal_err_resp
from app.models.restaurant import Restaurant
from app.models.product import Product
from app.models.serializers import RestaurantSchema,ProductSchema

restaurant_schema = RestaurantSchema()
product_schema = ProductSchema()


class RestaurantService:



    @staticmethod
    def register(data:dict,user:dict):
        """
            This method handles the restaurant register operation
        """
        name = data.get('name')
        user_id = user.get("id")
        is_owner = user.get("is_owner")

        if not (is_owner):
            return err_resp('Forbidden',"owner_403",403)
        if Restaurant.query.filter_by(name=name).first():
            return err_resp('A restaurant by this name already exists.',"name_409",409)

        try:

            restaurant = Restaurant(name=name,
                            joined_date=datetime.utcnow(),
                            owner=user_id)

            #DB
            db.session.add(restaurant)
            db.session.commit()

            restaurant_info = restaurant_schema.dump(restaurant) # Convert JSON format the user model


            res = message('True', 'Restaurant Registration Successful!')

            res['restaurant'] = restaurant_info
            return res,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_products(restaurant_id:int):




        if not Restaurant.query.filter_by(id=restaurant_id).first():
            return err_resp('Restaurant not found',"restaurant_404",404)


        restaurant = Restaurant.query.filter_by(id=restaurant_id).first()


        from .load_data import load_data
        if not (products := restaurant.products):
            return err_resp(message="Products not found",status=400)

        try:

            product_data = [load_data(product) for product in products]
            resp=message(True,"Products loaded successfully")
            resp['restaurant'] = restaurant.name
            resp["products"]=product_data
            return resp,200
        except Exception as e:
            #current_app.logger.error(e)
            return internal_err_resp()

class ProductService:

    @staticmethod
    def register(data:dict,user:dict):
        """
            This method handles the productregister operation
        """

        name = data.get("name")
        price = data.get("price")
        description = data.get("description")
        image_url = data.get("image_url")
        is_owner = user.get("is_owner")
        user_id = user.get("id")


        if not (is_owner):
            return err_resp('Forbidden',"owner_403",403)

        if not Restaurant.query.filter_by(owner=user_id).first():

            return err_resp('Restaurant not found',"restaurant_404",404)

        try:
            restaurant = Restaurant.query.filter_by(owner=user_id).first()

            product = Product(name=name,
                              price=price,
                              description=description,
                              image_url=image_url,
                              restaurant_id=restaurant.id)
            #DB
            db.session.add(product)
            db.session.commit()

            product_info = product_schema.dump(product) # Convert JSON format the user model


            res = message('True', 'Product Registration Successful!')

            res['product'] = product_info
            return res,200

        except Exception as e:
                current_app.logger.error(e)
                return internal_err_resp()
