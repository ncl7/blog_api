# src/shared/Authentication
import jwt
import os
import datetime
from flask import json, Response, request, g
from ..models.UserModel import UserModel


class Auth():
    """
    Auth Class
    """
