import os


from .database import db_session
from flask import Flask



def shutdown_session(exception=None):
    db_session.remove()

def create_app(config_file):
    app = Flask(__name__)

    config_path = os.path.join(os.getcwd(), 'config', config_file + '.py')
    app.config.from_pyfile(config_path)

    app.teardown_appcontext(shutdown_session)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)
    # TODO(Alex Z.) Don't for get to db_session.remove
   
    return app
