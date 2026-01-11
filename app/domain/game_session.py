# app/domain/game_session.py
import uuid
from datetime import datetime

class GameSession:
    # Initialize a GameSession instance
    def __init__(self, game_name: str, game_type: str, players: list):
        self.game_name = game_name
        self.game_type = game_type
        self.players = players
        self.is_active = True
        self.is_completed = False
        self.session_id = str(uuid.uuid4())
        self.start_time = datetime.now()
        self.end_time = None
        self.state = {}
        self.result = None
    
    def mark_completed(self, result: str):
        # Mark the game session as completed (win, loss, quit)
        self.is_completed = True
        self.is_active = False
        self.end_time = datetime.now()
        self.result = result

    def update_state(self, new_state: dict):
        # Update state by move that someone makes depending on game type
        self.state = new_state
        return self.to_dict()
    
    def to_dict(self) -> dict:
        # Convert the GameSession instance to a dictionary
        return {
            "game_name": self.game_name,
            "game_type": self.game_type,
            "players": self.players,
            "is_active": self.is_active,
            "is_completed": self.is_completed,
            "session_id": self.session_id,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "state": self.state,
            "result": self.result
        }