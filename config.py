from sqlalchemy import create_engine


class Config(object):
    SECRET_KEY="ClaveSecreta"
    SESSION_COKIE_SECURE=False


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://meliodas23#:root@127.0.0.1/bdidgs803'
    SQLALCHEMY_TRACK_MODIFICATIONS=False