from flask import Blueprint

from app.controllers.user.main import create_user
from app.controllers.user.main import delete_user
from app.controllers.user.main import edit_user
from app.controllers.user.main import view_user


user: Blueprint = Blueprint(name=__name__.split(".")[-1], import_name=__name__, url_prefix="/user")

user.add_url_rule(rule="/create", endpoint="create_user", view_func=create_user, methods=["POST"])
user.add_url_rule(rule="/delete", endpoint="delete_user", view_func=delete_user, methods=["POST"])
user.add_url_rule(rule="/edit", endpoint="edit_user", view_func=edit_user, methods=["POST"])
user.add_url_rule(rule="/<string:key>/view", endpoint="view_user", view_func=view_user, methods=["GET"])