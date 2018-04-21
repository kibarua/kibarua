import os 

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    ASTUSERNAME = "Dun"
    ASTAPI_KEY = "4506e82b61eeb95fbb51c4d8ea123cdcd55f72a1f8836effd2c32974476948fc"
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