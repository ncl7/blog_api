# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime
from .BlogpostModel import BlogpostSchema


class UserModel(db.Model):
    """
    User Model
    """
