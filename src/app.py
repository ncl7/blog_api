# src/app.py

from flask import Flask

from .config import app_config


def create_app(env_name):
    """
    Create app
    """
