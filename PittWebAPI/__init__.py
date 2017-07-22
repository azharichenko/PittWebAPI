import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_file):
    app = Flask(__name__)

    config_path = os.path.join(os.getcwd(), 'config', config_file + '.py')
    app.config.from_pyfile(config_path)

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
