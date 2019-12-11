# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime
from . import db


class UserModel(db.Model):
    """
    User Model
    """

# table name
