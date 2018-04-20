import os 

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    ASTUSERNAME = 'sandbox                                                                                                                                                                                                                                                                                                                                                                                                                      '
    ASTAPI_KEY = '3d9ca64e8d14a82d2a7afbfebd6189c99c297adbade83cd088eb31ce0ee27876'
    SECRET_KEY = "\x05y\xfc\xa3\xa5T\x07\xa7\x82\xdb\xe5-mK5\xebZl\xe5\xe3\xce[\x1bT"
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False



class ProConfig(Config):
    DEBUG =False


config = {
    'DEV':DevConfig,
    'PRO':ProConfig
}