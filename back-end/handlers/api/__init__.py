from flask import Blueprint

from .v1 import V1

API = Blueprint(name='api', url_prefix='/api', import_name=__name__)

API.register_blueprint(blueprint=V1)
