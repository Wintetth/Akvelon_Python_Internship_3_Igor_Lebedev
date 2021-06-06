from flask import Blueprint

from app.controllers.transaction.main import create_transaction
from app.controllers.transaction.main import delete_transaction
from app.controllers.transaction.main import edit_transaction
from app.controllers.transaction.main import view_transaction
from app.controllers.transaction.main import view_all_transactions
from app.controllers.transaction.main import grouped_transactions


transaction: Blueprint = Blueprint(name=__name__.split(".")[-1], import_name=__name__, url_prefix="/transaction/<string:key>")

transaction.add_url_rule(rule="/create", endpoint="create_transaction", view_func=create_transaction, methods=["POST"])
transaction.add_url_rule(rule="/delete/<int:transaction_id>", endpoint="delete_transaction", view_func=delete_transaction, methods=["POST"])
transaction.add_url_rule(rule="/edit/<int:transaction_id>", endpoint="edit_transaction", view_func=edit_transaction, methods=["POST"])
transaction.add_url_rule(rule="/view/<int:transaction_id>", endpoint="view_transaction", view_func=view_transaction, methods=["GET"])
transaction.add_url_rule(rule="/view_all", endpoint="view_all_transactions", view_func=view_all_transactions, methods=["GET"])
transaction.add_url_rule(rule="/grouped", endpoint="grouped_transactions", view_func=grouped_transactions, methods=["GET"])
