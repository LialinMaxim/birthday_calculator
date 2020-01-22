from flask import Flask
from flask_bootstrap import Bootstrap

from config import Config

bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)

    from app.birthday_calculator import bp as bp_birthday_calculator
    app.register_blueprint(bp_birthday_calculator)

    return app
