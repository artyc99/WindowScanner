from models.core import Config
from handlers import App


if __name__ == '__main__':
    config = Config(
        host='127.0.0.1',
        port=5000
    )
    app = App(config=config)
    app.run()
