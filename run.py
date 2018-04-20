from app import create_app , db
from flask_migrate import Migrate

from config import config


# This asumes dev run mode
app = create_app(config['DEV'])


migrate = Migrate(app, db)
