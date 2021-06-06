from flask import jsonify, request

from app.models.user import User
from app.models.transaction import Transaction


def create_transaction(key: str):
    user: User = User.get_or_none(key=key)

    if user is None:
        return (jsonify(message="You need to log in before."), 403)
        
    amount: str = request.form.get("amount", "")
    if not (amount.isdigit() and int(amount) > 0):
        return (jsonify(message="Transaction amount should be a digit greater than 0."), 400)

    transaction: Transaction = Transaction.create(user=user, amount=amount)

    return (
        jsonify(
            message="Transaction created.",
            amount=amount,
            date=transaction.date.strftime("%Y.%m.%d")
        ),
        201
    )

def delete_transaction(key: str):
    return (jsonify(message="Transaction deleted."), 201)

def edit_transaction(key: str):
    return (jsonify(message="Transaction edited."), 201)

def view_transaction(key: str):
    return (jsonify(message="Transaction viewed."), 200)

def view_all_transactions(key: str):
    return (jsonify(message="All transactions viewed."), 200)
    