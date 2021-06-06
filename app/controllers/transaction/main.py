from flask import jsonify


def create_transaction():
    return (jsonify(message="Transaction created."), 201)

def delete_transaction():
    return (jsonify(message="Transaction deleted."), 201)

def edit_transaction():
    return (jsonify(message="Transaction edited."), 201)

def view_transaction():
    return (jsonify(message="Transaction viewed."), 200)

def view_all_transactions():
    return (jsonify(message="All transactions viewed."), 200)
    