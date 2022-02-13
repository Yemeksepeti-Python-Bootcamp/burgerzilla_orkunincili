from marshmallow import Schema, fields
from marshmallow.validate import Regexp, Length

"""
We will provide request data with these schemas
"""

class LoginSchema(Schema):
    """ /auth/login method -> POST

    Parameters:
    - Email
    - Password (Str)
    """

    email = fields.Email(required=True, validate=[Length(max=64)])
    password = fields.Str(required=True, validate=[Length(min=8, max=128)])


class RegisterSchema(Schema):
    """ /auth/register method -> POST

    Parameters:
    - Email
    - First name (Str)
    - Last name (Str)
    - Password (Str)
    """

    email = fields.Email(required=True, validate=[Length(max=64)])
    first_name = fields.Str(required=True,validate=[Length(min=3)])
    last_name = fields.Str(required=True,validate=[Length(min=3)])
    password = fields.Str(required=True, validate=[Length(min=8, max=128)])
    is_owner = fields.Boolean(required=False)
