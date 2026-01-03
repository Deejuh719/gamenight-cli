# tests/domain/test_game.py
# Tests for TC-GN-DL-001, 002
import pytest
from app.domain.game import Game

def test_game_creation_with_valid_data():
    # Create a Game instance with valid data
    game = Game(name="Magic 8 Ball", game_type="fortune_telling", min_players=1, max_players=1)

    # Verify that the Game instance is created correctly
    assert game.name == "Magic 8 Ball"
    assert game.game_type == "fortune_telling"
    assert game.min_players == 1
    assert game.max_players == 1

def test_game_requires_name():
    # Attempt to create a Game instance without a name
    with pytest.raises(ValueError) as excinfo:
        Game(name="", game_type="fortune_telling", min_players=1, max_players=1)
    # Check that the appropriate exception is raised
    assert "Game name is required" in str(excinfo.value)

def test_game_requires_type():
    # Attempt to create a Game instance without a game type
    with pytest.raises(ValueError) as excinfo:
        Game(name="Magic 8 Ball", game_type="", min_players=1, max_players=1)
    # Check that the appropriate exception is raised
    assert "Game type is required" in str(excinfo.value)

def test_game_to_dict():
    # Create a Game instance and convert it to a dictionary
    game = Game(name="Magic 8 Ball", game_type="fortune_telling", min_players=1, max_players=1)
    # Create the expected dictionary representation
    expected_dict = {
        "name": "Magic 8 Ball",
        "game_type": "fortune_telling",
        "min_players": 1,
        "max_players": 1
    }
    # Verify that the to_dict method returns the expected dictionary
    assert game.to_dict() == expected_dict