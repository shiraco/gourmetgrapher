# coding:utf-8
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object("application.config.DevelopmentConfig")
    return app


app = create_app()

from application import views
