# app/routes/game_api.py
from flask import Blueprint, request, jsonify, current_app

game_api_bp = Blueprint('game_api', __name__, url_prefix='/api/games')

@game_api_bp.route('', methods=['GET'])
def list_games():
    games = current_app.game_service.list_games()
    return jsonify(games), 200