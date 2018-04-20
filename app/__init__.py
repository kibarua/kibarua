from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import africastalking

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_cors import CORS

db = SQLAlchemy()


from .models import User , Service , Client, Task

def create_app(config):
    app = Flask(__name__)
    # Load config
    app.config.from_object(config)
    
    # init db
    db.init_app(app)   
    CORS(app)
    africastalking.initialize(config.ASTUSERNAME, config.ASTAPI_KEY)

    from .views import api as  api_blueprints
    app.register_blueprint(api_blueprints)

    admin = Admin(app, name='Dashboard')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Service, db.session))
    admin.add_view(ModelView(Client, db.session))
    admin.add_view(ModelView(Task, db.session))
    return app
