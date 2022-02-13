from marshmallow import Schema, fields
from marshmallow.validate import Regexp, Length,Range

"""
We will provide request data with these schemas
"""



class OrderCreateSchema(Schema):
    """ /restaurant method -> POST

    Parameters:
    -user_id (Int)
    -product_id (Int)

    """


    user_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
