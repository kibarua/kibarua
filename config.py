import os 

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    ASTUSERNAME = "Neville Omangi"
    ASTAPI_KEY = "6d8f797048c2c04159ee4b79d13200aa2e54dc58ccec4ccc791fadb28d0c4f6f"
    SECRET_KEY = "\x05y\xfc\xa3\xa5T\x07\xa7\x82\xdb\xe5-mK5\xebZl\xe5\xe3\xce[\x1bT"
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False



class ProConfig(Config):
    DEBUG =False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False


config = {
    'DEV':DevConfig,
    'PRO':ProConfig
}