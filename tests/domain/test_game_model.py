# tests/domain/game_model.py
import pytest
from app.models.games import Game

def test_game_to_dict_includes_basic_fields():
    game = Game(id=1, name="trivia", description="Trivia Game", state={"round": 1})
    result = game.to_dict()
    assert result["id"] == 1
    assert result["name"] == "trivia"
    assert result["description"] == "Trivia Game"
    assert result["state"]["round"] == 1