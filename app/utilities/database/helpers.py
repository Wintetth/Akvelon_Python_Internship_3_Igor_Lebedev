from app.models.user import User
from app.models.transaction import Transaction


def create_tables():
    User.create_table()
    Transaction.create_table()
