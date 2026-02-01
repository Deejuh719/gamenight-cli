# app/services/game_service.py
from typing import List, Dict, Optional
from app.domain.game_session import GameSession

class GameService:
    # Games available to match the pre-existing CLI
    AVAILABLE_GAMES = [
        {"id": 1, "name": "Magic 8 Ball", "game_type": "Single Player", "min_players": 1, "max_players": 1},
        {"id": 2, "name": "Blackjack", "game_type": "Multiplayer", "min_players": 1, "max_players": 7},
        {"id": 3, "name": "Hangman", "game_type": "Single Player", "min_players": 1, "max_players": 1},
        {"id": 4, "name": "Bagels", "game_type": "Single Player", "min_players": 1, "max_players": 1},
        {"id": 5, "name": "Vigenere Cipher", "game_type": "Single Player", "min_players": 1, "max_players": 1},
        {"id": 6, "name": "Quick Draw", "game_type": "Single Player", "min_players": 1, "max_players": 1},
        {"id": 7, "name": "Terminal Hacker", "game_type": "Single Player", "min_players": 1, "max_players": 1},
        {"id": 8, "name": "Quit", "game_type": "Single Player", "min_players": 1, "max_players": 1},
    ]

    def __init__(self):
        # Initialize game sessions with empty storage
        self.game_sessions: Dict[str, GameSession] = {}

    def list_available_games(self) -> List[dict]:
        # Return list of available games
        return list(self.AVAILABLE_GAMES)

    def create_game_session(self, name: str) -> GameSession:
        # Create a new game session
        game_session = GameSession()
        game_session.name = name
        self.game_sessions[game_session.id] = game_session
        return game_session

    def get_game_session_by_id(self, session_id: str) -> Optional[GameSession]:
        # Retrieve a game session by its ID
        return self.game_sessions.get(session_id)

    def game_move(self, session_id: str, move: dict) -> None:
        # Process a game move for the specified session
        game_session = self.get_game_session_by_id(session_id)
        if not game_session:
            raise KeyError(f"Game session with ID {session_id} not found.")
        # Update the game session state based on the move
        game_session.update_state(move)
