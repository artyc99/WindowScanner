from flask import Blueprint

from .windows_table import WINDOWS_TABLE

V1 = Blueprint(name='v1', url_prefix='/v1', import_name=__name__)

V1.register_blueprint(blueprint=WINDOWS_TABLE)

