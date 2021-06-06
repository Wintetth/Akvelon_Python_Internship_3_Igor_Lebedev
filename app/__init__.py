from flask import Flask
from flask import jsonify

from app.controllers import user
from app.controllers import transaction
from app.controllers import forbidden
from app.controllers import not_found
from app.controllers import method_not_allowed
from app.controllers import internal_server_error


app: Flask = Flask(import_name=__name__)

app.register_error_handler(403, forbidden)
app.register_error_handler(404, not_found)
app.register_error_handler(405, method_not_allowed)
app.register_error_handler(500, internal_server_error)

app.register_blueprint(user)
app.register_blueprint(transaction)