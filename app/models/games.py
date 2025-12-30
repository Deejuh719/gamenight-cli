# app/models/games.py
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class Game:
    # Domain model for a Game w/ id, name, and optional description
    def __init__(self, id, name, description, state):
        self.id: int = id
        self.name: str = name
        self.description: Optional[str] = description
        self.state: Dict[str, Any] = state if state is not None else {}

    def to_dict(self) -> Dict[str, Any]:
        # Serialize to JSON-friendly dict
        return {"id": self.id,
                "name": self.name,
                "description": self.description,
                "state": self.state
                }
