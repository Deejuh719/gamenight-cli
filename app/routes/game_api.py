# app/routes/game_api.py
from flask import Blueprint, request, jsonify, current_app

game_api_bp = Blueprint('game_api', __name__, url_prefix='/api/games')

@game_api_bp.route('', methods=['GET'])
def list_games():
    games = current_app.game_service.list_available_games()
    return jsonify(games), 200

@game_api_bp.route('/sessions', methods=['POST'])
def create_game_session():
    data = request.get_json()
    required_fields = ['name', 'game_type', 'players']
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        session = current_app.game_service.create_game_session(data['name'], data['game_type'], data['players'])
        return jsonify(session), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@game_api_bp.route('/sessions/<session_id>', methods=['GET'])
def get_game_session(session_id):
    session = current_app.game_service.get_session_by_id(session_id)
    if not session:
        return jsonify({"error": "Game session not found"}), 404
    return jsonify(session), 200

@game_api_bp.route('/sessions/<session_id>/moves', methods=['POST'])
def make_move(session_id):
    data = request.get_json()

    if not data or 'move' not in data:
        return jsonify({"error": "Missing required field: 'move'"}), 400

    try:
        session = current_app.game_service.make_move(session_id, data['move'])
        return jsonify(session), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400