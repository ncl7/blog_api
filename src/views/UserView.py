# /src/views/UserView

from flask import request, json, Response, Blueprint
# from ..models.UserModel import UserModel, UserSchema
# from ..shared.Authentication import Auth

user_api = Blueprint('users', __name__)
# user_schema = UserSchema()

# @user_api.route('/', methods=['POST'])
# def create():
