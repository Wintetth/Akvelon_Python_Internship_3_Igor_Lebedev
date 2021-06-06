from flask import jsonify, request

from peewee import ModelSelect

from pandas import DataFrame

from datetime import datetime

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
    user: User = User.get_or_none(key=key)

    if user is None:
        return (jsonify(message="You need to log in before."), 403)

    transaction: Transaction = Transaction.get_or_none(transaction_id=transaction_id, user=user)
    if transaction is None:
        return (jsonify(message="Transaction was not found."), 404)
    
    return (
        jsonify(
            message="Transaction viewed.",
            amount=transaction.amount,
            date=transaction.date.strftime("%Y.%m.%d")
        ),
        201
    )

def view_all_transactions(key: str, filter: str = None):
    user: User = User.get_or_none(key=key)

    if user is None:
        return (jsonify(message="You need to log in before."), 403)

    transactions: ModelSelect = Transaction.select().where(Transaction.user == user)

    if len(filter) == 10 and len(filter.split(".")) == 3 and all(map(lambda x: x.isdigit(), filter.split("."))):
        transactions = transactions.select().where(Transaction.date == datetime.strptime(filter, "%Y.%m.%d"))
    elif filter == "income":
        transactions = transactions.select().where(Transaction.amount > 0)
    elif filter == "outcome":
        transactions = transactions.select().where(Transaction.amount < 0)
        
    if not transactions.exists():
        return (jsonify(message="No transactions were found."), 404)

    return (
        jsonify(
            message="All transactions viewed.",
            transactions=[
                {
                    "id": transaction.transaction_id,
                    "amount": transaction.amount,
                    "date": transaction.date.strftime("%Y.%m.%d")
                } for transaction in transactions
            ]
        ),
        201
    )

def grouped_transactions(key: str):
    user: User = User.get_or_none(key=key)

    if user is None:
        return (jsonify(message="You need to log in before."), 403)

    transactions: ModelSelect = Transaction.select().where(Transaction.user == user)
    if not transactions.exists():
        return (jsonify(message="No transactions were found."), 404)
    
    transactions_frame: DataFrame = DataFrame(data=[
        {
            "amount": transaction.amount,
            "date": transaction.date.strftime("%Y.%m.%d")
        } for transaction in transactions
    ])

    transactions_frame = transactions_frame.groupby("date").agg({"amount": "sum"}).reset_index()

    return (
        jsonify(
            message="Grouped transactions viewed.",
            transactions=[
                {
                    "date": row["date"],
                    "amount": row["amount"]
                } for (_, row) in transactions_frame.iterrows()
            ]
        ),
        201
    )
