from flask import jsonify

from app.utilities.fibonacci import fibonacci


def fibonacci_controller(n: int = None):
    if n == None:
        return (jsonify(message="You need to enter 'n' first."), 400)
    if n < 0:
        return (jsonify(message="Incorrect number was provided"), 400)

    result: int = fibonacci(n)

    return (jsonify(message="Nth Fibonacci sequence number was calculated.", result=result), 200)
    