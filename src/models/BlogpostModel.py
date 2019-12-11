# src/models/BlogPostModel.py
from . import db
import datetime

from marshmallow import fields, Schema


class BlogpostModel(db.Model):
  """
  Blogpost Model
  """
