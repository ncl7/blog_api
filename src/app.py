# src/app.py

from flask import Flask

# from .config import app_config
from .models import db, bcrypt

# import user_api blueprint
from .views.UserView import user_api as user_blueprint # add this line


def create_app(env_name):
    """
    Create app
    """
