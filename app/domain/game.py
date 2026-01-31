# app/domain/game.py
class Game:
    #Initialize Game object with validation
    def __init__(self, id:int, name:str, game_type:str,  min_players:int, max_players:int):
        # Validation ensures no empty fields
        if not name or name.strip() == "":
            raise ValueError("Game name cannot be empty.")
        if game_type == None or game_type.strip() == "":
            raise ValueError("Game type cannot be empty.")
        if min_players < 1:
            raise ValueError("Minimum players must be at least 1.")
        if max_players < min_players:
            raise ValueError("Maximum players cannot be less than the minimum players.")
        if id < 0:
            raise ValueError("Game ID cannot be negative.")
        # Assign values
        self.id = id
        self.name = name
        self.game_type = game_type
        self.min_players = min_players
        self.max_players = max_players

# Validate the Game object
    def is_valid(self) -> bool:
        # Follows same validation as init, returns boolean
        if not self.name or self.name.strip() == "":
            return False
        if self.game_type == None or self.game_type.strip() == "":
            return False
        if self.min_players < 1:
            return False
        if self.max_players < self.min_players:
            return False
        return True

# Return games as dictionary
    def return_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "game_type": self.game_type,
            "min_players": self.min_players,
            "max_players": self.max_players,
        }