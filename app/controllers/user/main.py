from flask import jsonify


def create_user():
    return (jsonify(message="User created."), 201)

def delete_user():
    return (jsonify(message="User deleted."), 201)

def edit_user():
    return (jsonify(message="User edited."), 201)

def view_user():
    return (jsonify(message="User viewed."), 200)
