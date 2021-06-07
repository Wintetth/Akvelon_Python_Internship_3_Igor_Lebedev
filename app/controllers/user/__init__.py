from flask import Blueprint, render_template

from app.controllers.user.main import create_user
from app.controllers.user.main import delete_user
from app.controllers.user.main import edit_user
from app.controllers.user.main import view_user


def user():
    return render_template("user.html")

user: Blueprint = Blueprint(name=__name__.split(".")[-1], import_name=__name__, url_prefix="/user")

user.add_url_rule(rule="/", endpoint="user", view_func=user, methods=["GET"])
user.add_url_rule(rule="/create", endpoint="create_user", view_func=create_user, methods=["POST"])
user.add_url_rule(rule="/delete", endpoint="delete_user", view_func=delete_user, methods=["POST"])
user.add_url_rule(rule="/edit", endpoint="edit_user", view_func=edit_user, methods=["POST"])
user.add_url_rule(rule="/<string:key>/view", endpoint="view_user_by_key", view_func=view_user, methods=["GET"])
user.add_url_rule(rule="/view", endpoint="view_user_by_password", view_func=view_user, methods=["POST"])
