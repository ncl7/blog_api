# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime
from ..app import bcrypt


class UserModel(db.Model):
    """
    User Model
    """


# table name
