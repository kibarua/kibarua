import os 

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    ASTUSERNAME = 'sandbox                                                                                                                                                                                                                                                                                                                                                                                                                      '
    ASTAPI_KEY = '33115a3b3e74dffac8476b04d6ec6d7fa547c7502eef8d24968f8bd23d07f31c'
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