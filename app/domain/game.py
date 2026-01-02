class Game:
    def __init__(self, name: str, game_type: str, min_players: int, max_players: int):
        # Create ValueError if name or type is missing
        if not name:
            raise ValueError("Game name is required")
        if not game_type:
            raise ValueError("Game type is required")

        # Initialize the attributes
        self.name = name
        self.game_type = game_type
        self.min_players = min_players
        self.max_players = max_players
    
    def is_valid(self) -> bool:
        # Check if the Game instance is valid
        return bool(self.name and self.game_type)

    def to_dict(self) -> dict:
        # Convert the Game instance to a dictionary
        return {
            "name": self.name,
            "game_type": self.game_type,
            "min_players": self.min_players,
            "max_players": self.max_players
        }