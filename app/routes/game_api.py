# app/routes/game_api.py
from flask import Blueprint, request, jsonify, current_app

game_api_bp = Blueprint('game_api', __name__, url_prefix='/api/games')

@game_api_bp.route('', methods=['GET'])
def list_games():
    ''' Returns a jsonified list of available games
        i.e.: [{"id": 1, "name": "Magic 8 Ball", "type": "fortune_telling"}, 
                {"id": 2, "name": "Blackjack", "type": "card_game"}...]
    '''
    games = current_app.game_service.list_available_games()
    return jsonify(games), 200

@game_api_bp.route('/sessions', methods=['POST'])
def create_game_session():
    # Creates a new game session with unique ID and details
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
    # Retrieves details of a specific game session by ID
    session = current_app.game_service.get_session_by_id(session_id)
    if not session:
        return jsonify({"error": "Game session not found"}), 404
    return jsonify(session), 200

@game_api_bp.route('/sessions/<session_id>/moves', methods=['POST'])
def make_move(session_id):
    # Updates the game session state based on the move made by a player or game
    data = request.get_json()

    if not data or 'move' not in data:
        return jsonify({"error": "Missing required field: 'move'"}), 400

    try:
        session = current_app.game_service.make_move(session_id, data['move'])
        return jsonify(session), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@game_api_bp.route('/sessions/<session_id>/end', methods=['POST'])
def end_game_session(session_id):
    # Ends the specified game session
    data = request.get_json()
    if not data or 'result' not in data:
        return jsonify({"error": "Missing required field: 'result'"}), 400

    try:
        session = current_app.game_service.end_game_session(session_id, data['result'])
        return jsonify(session), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400