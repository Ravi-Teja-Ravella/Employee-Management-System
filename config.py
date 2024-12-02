from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from urllib.parse import quote_plus

class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')  # Replace 'your-secret-key' with a strong random value
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:%s@localhost/CS480Project" % quote_plus("")


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
