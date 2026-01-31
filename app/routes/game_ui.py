import random
from flask import Blueprint, render_template, request, redirect, url_for, current_app

game_ui_bp = Blueprint('game_ui', __name__, url_prefix='/games', template_folder='app/templates')

GAME_TITLES = {
    'magic_8_ball' : 'Magic 8 Ball',
    'blackjack' : 'Black Jack',
    'hangman' : 'Hangman',
    'bagels' : 'Bagels',
    'vignerecipher' : 'Vigenère Cipher',
    'quickdraw' : 'Quick Draw',
    'terminalhack' : 'Terminal Hacker',
}

@game_ui_bp.route('', methods=['GET'])
def game_select():
    # Render game selection page
    games = current_app.game_service.list_available_games()
    return render_template('game_selection.html', games=games)

@game_ui_bp.route('/<game_name>/', methods=['GET', 'POST'])
def start_game(game_name):
    game_service = current_app.game_service
    if request.method == 'POST':
        # Start a new game session
        session_id = game_service.start_game_session(game_name)
        return redirect(url_for('game_ui.play_game', game_name=game_name, session_id=session_id))
    
    # Render game start page
    game_title = GAME_TITLES.get(game_name, 'Unknown Game')
    return render_template('start_game.html', game_name=game_name, game_title=game_title)

@game_ui_bp.route('/<game_name>/<session_id>', methods=['GET', 'POST'])
def play_game(game_name, session_id):
    game_service = current_app.game_service
    game_state = game_service.get_game_state(session_id)
    
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        game_state = game_service.process_user_input(session_id, user_input)
        
        if game_state['is_over']:
            return redirect(url_for('game_ui.game_over', game_name=game_name, session_id=session_id))
    
    return render_template('play_game.html', game_name=game_name, session_id=session_id, game_state=game_state)

@game_ui_bp.route('/<game_name>/<session_id>/move', methods=['GET'])
def make_move(game_name, session_id):
    game_service = current_app.game_service
    game_state = game_service.get_game_state(session_id)
    
    if game_state['requires_move']:
        move = random.choice(game_state['available_moves'])
        game_state = game_service.process_user_input(session_id, move)
        
        if game_state['is_over']:
            return redirect(url_for('game_ui.game_over', game_name=game_name, session_id=session_id))
    
    return redirect(url_for('game_ui.play_game', game_name=game_name, session_id=session_id))

@game_ui_bp.route('/<game_name>/<session_id>/over', methods=['GET'])
def game_over(game_name, session_id):
    game_service = current_app.game_service
    game_state = game_service.get_game_state(session_id)
    
    return render_template('game_over.html', game_name=game_name, session_id=session_id, game_state=game_state)