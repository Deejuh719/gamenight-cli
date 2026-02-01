# app/domain/game_session.py
import uuid

class GameSession:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.name = ""
        self.players = []
        self.status = "active"
        self.state = {}

    def update_state(self, new_state):
        self.state.update(new_state)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "players": self.players,
            "status": self.status,
            "state": self.state,
        }