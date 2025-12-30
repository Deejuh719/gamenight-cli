# app/__init__.py
from flask import Flask

def create_app(service=None):
    app = Flask(__name__)

    return app