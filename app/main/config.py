import os

from decouple import config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'database')


def get_database_uri(database_type, database_uri):
    if database_type == 'sqlite':
        return 'sqlite:///' + os.path.join(DATABASE_PATH, database_uri)
    else:
        return database_uri


class BaseConfig(object):
    SECRET_KEY = config('SECRET_KEY', default="123456")
    SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = get_database_uri(config("DEV_DB_TYPE"), config("DEV_DB"))
    DEBUG = True


configuration = {
    "development": DevelopmentConfig
}
