from marshmallow import Schema, fields
from marshmallow.validate import Regexp, Length,Range

"""
We will provide request data with these schemas
"""



class RegisterRestaurantSchema(Schema):
    """ /restaurant method -> POST

    Parameters:
    -Name (Str)

    """


    name = fields.Str(required=True,validate=[Length(min=3)])


class RegisterProductSchema(Schema):
    """ /restaurant/prodcut method -> POST

    Parameters:
    -Name (Str)
    -Price (Float)
    -Desc (Str)
    -Url  (Url)

    """

    name = fields.Str(required=True,validate=[Length(min=3)])
    price = fields.Float(required=True,validate=[Range(min=0.0)])
    description = fields.Str(required=True)
    image_url = fields.URL(required=True)
