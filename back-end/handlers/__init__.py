from flask import Flask

from models.core import Config
from .api import API


class App:
    def __init__(self, config: Config):
        # logger.info('Init Flask application')

        self.__config = config

        self.__app = Flask(import_name=__name__)
        self.__app.secret_key = self.__config.secret_key

        self.__register_handlers()

    def __register_handlers(self):
        self.__app.register_blueprint(blueprint=API)

    def run(self):
        # logger.info('Run Flask application')

        self.__app.run(
            host=self.__config.host,
            port=self.__config.port
        )
