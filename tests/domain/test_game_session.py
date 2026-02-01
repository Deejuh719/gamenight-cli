# tests/domain/test_game_session.py
import pytest
from app.domain.game_session import GameSession

# Focuses on test GN-DL-003 GameSession initialization
def test_game_session_initialization():
    """
    Ensures that GameSession initializes with:
    - A unique session ID
    - An empty list of players (will update when Player entity is implemented)
    - Session status is 'active'
    """
    game_session = GameSession()
    assert game_session.id is not None
    assert game_session.players == []
    assert game_session.status == "active"

# Test for unique IDs
def test_game_session_unique_id():
    game_session1 = GameSession()
    game_session2 = GameSession()
    assert game_session1.id != game_session2.id

# Test for status change (if applicable in future implementations)
def test_game_session_status_change():
    game_session = GameSession()
    game_session.status = "completed"
    assert game_session.status == "completed"

    game_session.status = "active"
    assert game_session.status == "active"

    game_session.status = "win"
    assert game_session.status == "win"

# Test state mgmt for moves in games like new rounds after winning
# and letters guessed in hangman
def test_game_session_state_change():
    # Initiate game session, create a round to update state
    game_session = GameSession()
    game_session.update_state({"round": 1, "scores": {}})
    assert game_session.state == {"round": 1, "scores": {}}
    # Update state to round 2
    game_session.update_state({"round": 2, "scores": {}})
    assert game_session.state == {"round": 2, "scores": {}}
    # Create a new game session and update guesses
    game_session = GameSession()
    game_session.update_state({"guesses": ["a", "b", "c"]}) # update state["guesses"]
    assert game_session.state == {"guesses": ["a", "b", "c"]}

# Test that game session returns a dict
def test_game_session_to_dict():
    game_session = GameSession()
    session_dict = game_session.to_dict()
    assert isinstance(session_dict, dict)
    assert session_dict["id"] == game_session.id
    assert session_dict["name"] == game_session.name
    assert session_dict["players"] == game_session.players
    assert session_dict["status"] == game_session.status
    assert session_dict["state"] == game_session.state
