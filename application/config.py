# coding:utf-8
import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "/S97ojVXKgKGNyaHvz6evbGwkB2C@2D-X.grmR9LESkTNR5q"
    SESSION_COOKIE_NAME = "_sid"
    UPLOAD_DIR = os.path.join("/Users/shiraishi/workspace/python/gourmetgrapher/application/static", "upload")


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
