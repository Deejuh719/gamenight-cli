# app/__init__.py

from flask import Flask
from app.health import register_health_route
def create_app():
    app = Flask(__name__)
    register_health_route(app)
    return app