# src/app.py

from flask import Flask

from .config import app_config
from .models import db, bcrypt


def create_app(env_name):
    """
    Create app
    """
