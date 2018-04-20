from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    # Load config
    app.config.from_object(config)
    
    # init db
    db.init_app(app)

    return app
