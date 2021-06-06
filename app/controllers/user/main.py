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
    key: str = request.form.get("key", "")
    user: User = User.get_or_none(key=key)

    if user is None:
        return (jsonify(message="You need to log in before."), 403)

    email: str = request.form.get("email", "")
    if len(email) != 0:
        if "@" not in email or "." not in email:
            return (jsonify(message="Incorrect email was provided."), 400)
        if not email.isascii():
            return (jsonify(message="Email should consist of latin letters or numbers only."), 400)
        if User.select().where(User.email == email).exists():
            return (jsonify(message="User with this email already exists."), 400)
        user.key = email.split("@")[0] + "-" + str(abs(hash(user.password)))
        user.email = email

    password: str = request.form.get("password", "")
    if len(password) != 0:
        if len(password) < 8:
            return (jsonify(message="Password should contain at least 8 charachters."), 400)
        if not password.isascii():
            return (jsonify(message="Email should consist of latin letters or numbers only."), 400)
        user.key = user.email.split("@")[0] + "-" + str(abs(hash(password)))
        user.password = password

    first_name: str = request.form.get("first_name", "")
    if len(first_name) != 0:
        user.first_name = first_name

    last_name: str = request.form.get("last_name", "")
    if len(last_name) != 0:
        user.last_name = last_name

    user.save()

    return (
        jsonify(
            message="User edited.",
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            key=user.key
        ),
        201
    )

def view_user(key: str = None):
    if request.method == "GET":
        user: User = User.get_or_none(key=key)
    else:
        user: User = User.get_or_none(email=request.form.get("email", ""), password=request.form.get("password", ""))

    if user is None:
        return (jsonify(message="You need to log in before."), 403)

    return (
        jsonify(
            message="User viewed.",
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            key=user.key
        ),
        200
    )
