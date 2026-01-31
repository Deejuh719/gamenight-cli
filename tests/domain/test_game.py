# tests/domain/test_game.py
import pytest
from app.domain.game import Game

"""
Covers TC-GN-DL-001 and TC-GN-DL-002 for initialization 
    of Game Model with valid data.
"""
def test_game_initialization_with_valid_data():
    # Assure that a Game object is correctly initialized with valid data
    game = Game(
        id=1,
        name="Magic 8 Ball",
        game_type="Single Player",
        min_players=1,
        max_players=1,
    )
    assert game.id == 1
    assert game.name == "Magic 8 Ball"
    assert game.min_players == 1
    assert game.max_players == 1
    assert game.game_type == "Single Player"
    assert game.is_valid()

def test_game_requires_name():
    with pytest.raises(ValueError):
        Game(
            id=1,
            name="",
            game_type="Single Player",
            min_players=1,
            max_players=1,
        )

def test_game_requires_game_type():
    with pytest.raises(ValueError):
        Game(
            id=1,
            name="Magic 8 Ball",
            game_type="",
            min_players=1,
            max_players=1,
        )

def test_game_min_players_at_least_one():
    with pytest.raises(ValueError):
        Game(
            id=1,
            name="Magic 8 Ball",
            game_type="Single Player",
            min_players=0,
            max_players=1,
        )

def test_game_max_players_not_less_than_min_players():
    with pytest.raises(ValueError):
        Game(
            id=1,
            name="Magic 8 Ball",
            game_type="Single Player",
            min_players=2,
            max_players=1,
        )

def test_game_id_not_negative():
    with pytest.raises(ValueError):
        Game(
            id=-1,
            name="Magic 8 Ball",
            game_type="Single Player",
            min_players=1,
            max_players=1,
        )

def test_return_dict():
    game = Game(
        id=1,
        name="Magic 8 Ball",
        game_type="Single Player",
        min_players=1,
        max_players=1,
    )
    game_dict = game.return_dict()
    expected_dict = {
        "id": 1,
        "name": "Magic 8 Ball",
        "game_type": "Single Player",
        "min_players": 1,
        "max_players": 1,
    }
    assert game_dict == expected_dict