# app/services/game_service.py
from typing import Dict, List, Optional
from app.domain.game import Game
from app.domain.game_session import GameSession

class GameService:
    # Dict of available games
    AVAILABLE_GAMES = {
        1: {"name": "Magic 8 Ball", "game_type": "fortune_telling", "min_players": 1, "max_players": 1},
        2: {"name": "Blackjack", "game_type": "card_game", "min_players": 1, "max_players": 7},
        3: {"name": "Hangman", "game_type": "guessing", "min_players": 1, "max_players": 4},
        4: {"name": "Bagels", "game_type": "guessing", "min_players": 1, "max_players": 1},
        5: {"name": "Vigenere Cipher", "game_type": "encryption", "min_players": 1, "max_players": 1},
        6: {"name": "Quick Draw", "game_type": "reaction", "min_players": 1, "max_players": 1},
        7: {"name": "Terminal Hacker", "game_type": "puzzle", "min_players": 1, "max_players": 1},
    }

    def __init__(self):
        # Initialize an empty dictionary to store game sessions
        self.sessions: Dict[str, GameSession] = {}

    def list_available_games(self) -> List[str]:
        # Return a list of available game names
        return [
                    {"id": game_id, "name": info["name"], "type": info["type"]}
                    for game_id, info in self.AVAILABLE_GAMES.items()
                ]
    def create_game_session(self, game_name: str, players: List[str]) -> dict:
        # Create a new game session
        game_info = next((info for info in self.AVAILABLE_GAMES.values() if info["name"] == game_name), None)
        if not game_info:
            raise ValueError(f"Game '{game_name}' is not available.")

        session = GameSession(
            game_name=game_info["name"],
            game_type=game_info["game_type"],
            players=players
        )
        self.sessions[session.session_id] = session
        return session.to_dict()

    def get_session_by_id(self, session_id: str) -> Optional[dict]:
        # Retrieve a game session by its ID
        session = self.sessions.get(session_id)
        if session:
            return session.to_dict()
        return None

    def make_move(self, session_id: str, move: dict) -> Optional[dict]:
        # Make a move in the specified game session
        session = self.sessions.get(session_id)
        if not session or not session.is_active:
            return None

        session.update_state(move)
        return session.to_dict()

    def end_game_session(self, session_id: str, result: str) -> Optional[dict]:
        # End the specified game session
        session = self.sessions.get(session_id)
        if not session or not session.is_active:
            return None

        session.mark_completed(result)
        return session.to_dict()