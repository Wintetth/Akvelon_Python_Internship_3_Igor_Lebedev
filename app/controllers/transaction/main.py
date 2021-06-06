from flask import jsonify, request

from app.models.user import User
from app.models.transaction import Transaction


def create_transaction(key: str):
    user: User = User.get_or_none(key=key)

    if user is None:
        return (jsonify(message="You need to log in before."), 403)
        
    try:
        amount: float = float(request.form.get("amount", ""))
    except ValueError:
        return (jsonify(message="Transaction amount should be a digit."), 400)

    transaction: Transaction = Transaction.create(user=user, amount=amount)

    return (
        jsonify(
            message="Transaction created.",
            amount=amount,
            date=transaction.date.strftime("%Y.%m.%d")
        ),
        201
    )

def delete_transaction(key: str, transaction_id: int):
    user: User = User.get_or_none(key=key)

    if user is None:
        return (jsonify(message="You need to log in before."), 403)

    transaction: Transaction = Transaction.get_or_none(transaction_id=transaction_id, user=user)
    if transaction is None:
        return (jsonify(message="Transaction was not found."), 404)

    transaction.delete_instance()

    return (jsonify(message="Transaction deleted."), 201)

def edit_transaction(key: str, transaction_id: int):
    user: User = User.get_or_none(key=key)

    if user is None:
        return (jsonify(message="You need to log in before."), 403)

    transaction: Transaction = Transaction.get_or_none(transaction_id=transaction_id, user=user)
    if transaction is None:
        return (jsonify(message="Transaction was not found."), 404)

    try:
        amount: float = float(request.form.get("amount", ""))
    except ValueError:
        return (jsonify(message="Transaction amount should be a digit."), 400)

    transaction.amount = amount
    transaction.save()

    return (
        jsonify(
            message="Transaction edited.",
            amount=amount,
            date=transaction.date.strftime("%Y.%m.%d")
        ),
        201
    )

def view_transaction(key: str, transaction_id: int):
    return (jsonify(message="Transaction viewed."), 200)

def view_all_transactions(key: str):
    return (jsonify(message="All transactions viewed."), 200)
    