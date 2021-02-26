"""
This script generates the app, imports configuration and initializes it
Then it sets the blueprint
"""

from flask import Flask
from .extensions import db
from .routes import short


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    # app.config['DEBUG'] = True
    
    app.config.from_pyfile(config_file)
    
    db.init_app(app)
    
    app.register_blueprint(short)

    return app