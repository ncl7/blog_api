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
    # app initiliazation
    #####################
    # existing code remain #
    ######################
    return custom_response(data, 201)


# add this function
@blogpost_api.route('/', methods=['GET'])
def get_all():
    """
  Get All Blogposts
  """
    posts = BlogpostModel.get_all_blogposts()
    data = blogpost_schema.dump(posts, many=True).data
    return custom_response(data, 200)

# app initiliazation
#####################
# existing code remain #
######################
