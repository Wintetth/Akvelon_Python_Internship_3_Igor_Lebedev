from flask import jsonify


def forbidden(_):
    return (jsonify(message="Forbidden."), 403)

def not_found(_):
    return (jsonify(message="Not found."), 404)

def method_not_allowed(_):
    return (jsonify(message="Method not allowed."), 405)

def internal_server_error(_):
    return (jsonify(message="Internal server error."), 500)