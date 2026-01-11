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
        # Initialize the GameService with an empty sessions dictionary
        self.sessions: Dict[str, GameSession] = {}

    def list_available_games(self) -> List[str]:
        # Return a list of available game names
        return [
                    {"id": game_id, "name": info["name"], "type": info["game_type"]}
                    for game_id, info in self.AVAILABLE_GAMES.items()
                ]
    def create_game_session(self, game_name: str, game_type: str, players: List[str]) -> dict:
        # Create new game session
        game_info = next((info for info in self.AVAILABLE_GAMES.values() if info["name"] == game_name and info["game_type"] == game_type), None)
        if not game_info:
            raise ValueError("Invalid game name or type")
        # Initialize new game session (round 1, 2, etc.)
        session = GameSession(game_name, game_type, players)
        self.sessions[session.session_id] = session
        return session.to_dict()

    def get_session_by_id(self, session_id: str) -> Optional[dict]:
        # Retrieve a game session by its ID (if it exists)
        if session_id in self.sessions:
            return self.sessions[session_id].to_dict()
        return None

    def make_move(self, session_id: str, move: dict) -> Optional[dict]:
        # Update the game session state based on the move (by game type)
        session = self.sessions.get(session_id)
        if not session or not session.is_active:
            return None
        return session.update_state(move)

    def end_game_session(self, session_id: str, result: str) -> Optional[dict]:
        # End the specified game session
        session = self.sessions.get(session_id)
        if not session or not session.is_active:
            return None

        session.mark_completed(result)
        return session.to_dict()