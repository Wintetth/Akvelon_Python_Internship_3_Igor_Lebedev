from flask import jsonify, request

from app.models.user import User


def create_user():
    email: str = request.form.get("email", "")
    if "@" not in email or "." not in email:
        return (jsonify(message="Incorrect email was provided."), 400)
    if not email.isascii():
        return (jsonify(message="Email should consist of latin letters or numbers only."), 400)
    if User.select().where(User.email == email).exists():
        return (jsonify(message="User with this email already exists."), 400)
    
    password: str = request.form.get("password", "")
    if len(password) < 8:
        return (jsonify(message="Password should contain at least 8 charachters."), 400)
    if not password.isascii():
        return (jsonify(message="Email should consist of latin letters or numbers only."), 400)

    first_name: str = request.form.get("first_name", "")
    if len(first_name) == 0:
        return (jsonify(message="First name was not provided."), 400)

    last_name: str = request.form.get("last_name", None)

    key: str = email.split("@")[0] + "-" + str(abs(hash(password)))

    _ = User.create(first_name=first_name, last_name=last_name, email=email, password=password, key=key)

    return (
        jsonify(
            message="User created.",
            first_name=first_name,
            last_name=last_name,
            email=email,
            key=key
        ),
        201
    )

def delete_user():
    return (jsonify(message="User deleted."), 201)

def edit_user():
    return (jsonify(message="User edited."), 201)

def view_user(key: str):
    return (jsonify(message="User viewed."), 200)
