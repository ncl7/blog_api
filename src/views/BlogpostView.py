# /src/views/BlogpostView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.BlogpostModel import BlogpostModel, BlogpostSchema

blogpost_api = Blueprint('blogpost_api', __name__)
blogpost_schema = BlogpostSchema()


@blogpost_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
    """
  Create Blogpost Function
  """
    return custom_response(data, 201)


@blogpost_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
    """
  Create Blogpost Function
  """
    return custom_response(data, 201)


@blogpost_api.route('/<int:blogpost_id>', methods=['GET'])
def get_one(blogpost_id):
    """
  Get A Blogpost
  """
    post = BlogpostModel.get_one_blogpost(blogpost_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = blogpost_schema.dump(post).data
    return custom_response(data, 200)
