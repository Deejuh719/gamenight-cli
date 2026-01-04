# app/__init__.py
from flask import Flask
from app.services.game_service import GameService

def create_app(game_service=None):
    # Create Flask app
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-to-change'
    app.config['TESTING'] = False

    # Dependency Injection for GameService
    if game_service is None:
        game_service = GameService()
    app.game_service = game_service

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return {"error": "Not Found"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Internal Server Error"}, 500

    return app
