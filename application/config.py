# coding:utf-8


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "/S97ojVXKgKGNyaHvz6evbGwkB2C@2D-X.grmR9LESkTNR5q"
    SESSION_COOKIE_NAME = "_sid"
    UPLOAD_DIR = "/tmp/"


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    UPLOAD_DIR = "/tmp/"


class DevelopmentConfig(Config):
    DEBUG = True
    UPLOAD_DIR = "/Users/shiraishi/workspace/python/gourmetgrapher/application/static/upload"


class TestingConfig(Config):
    TESTING = True
