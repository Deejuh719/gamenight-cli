# tests/domain/test_game_session.py
# Tests for TC-GN-DL-003, 004
import pytest
from app.domain.game_session import GameSession

def test_game_session_creation_with_valid_data():
    # Create a GameSession instance with valid data
    session = GameSession(game_name="Magic 8 Ball", game_type="fortune_telling", players=["Alice"])

    # Verify that the GameSession instance is created correctly
    assert session.game_name == "Magic 8 Ball"
    assert session.game_type == "fortune_telling"
    assert session.players == ["Alice"]
    assert session.is_active is True
    assert session.is_completed is False
    assert session.session_id is not None
    assert len(session.session_id) > 0

def test_game_session_generates_unique_session_id():
    # Create two GameSession instances
    session1 = GameSession(game_name="Magic 8 Ball", game_type="fortune_telling", players=["Alice"])
    session2 = GameSession(game_name="Magic 8 Ball", game_type="fortune_telling", players=["Bob"])

    # Verify that the session IDs are unique
    assert session1.session_id != session2.session_id

def test_game_session_is_completed():
    # Create a GameSession instance
    session = GameSession(game_name="Hangman", game_type="guessing", players=["Alice"])

    # Set the is_completed attribute to True
    session.mark_completed(result="win")

    # Verify that the is_completed attribute is True
    assert session.is_completed is True
    assert session.result == "win"
    assert session.is_active is False

def test_game_session_update_state():
    # Create GameSession instance
    session = GameSession(game_name="Hangman", game_type="guessing", players="Alice")
    # Update the session state to active
    session.update_state({"word": "python", "attempts_left": 5, "guessed_letters": ["p", "y"]})
    # Verify that the state is updated correctly
    assert session.state["word"] == "python"
    assert session.state["attempts_left"] == 5
    assert session.state["guessed_letters"] == ["p", "y"]

def test_game_session_to_dict():
    # Create a GameSession instance
    session = GameSession(game_name="Magic 8 Ball", game_type="fortune_telling", players=["Alice"])
    # Convert the GameSession instance to a dictionary
    session_dict = session.to_dict()
    # Verify that the dictionary contains the correct data
    assert session_dict["game_name"] == "Magic 8 Ball"
    assert session_dict["game_type"] == "fortune_telling"
    assert session_dict["players"] == ["Alice"]
    assert session_dict["is_active"] is True
    assert session_dict["is_completed"] is False
    assert session_dict["session_id"] == session.session_id
    assert session_dict["state"] == {}
    assert session_dict["result"] is None