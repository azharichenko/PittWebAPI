"""Testing Flask Configuration"""

import os

DEBUG = False
TESTING = True
SECRET_KEY = 'hidden'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    os.path.dirname(__file__), '../data-dev.sqlite3'
)
