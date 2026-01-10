# tests/services/test_game_service.py
import pytest
import app.services.game_service as GameService

@pytest.fixture
def game_service():
    game_service = GameService.GameService()
    return game_service

def test_list_available_games(game_service):
    # Should list all available games (currently 7)
    games = game_service.list_available_games()

    assert len(games) == 7
    for game in games:
        assert game["id"] is not None
        assert game["name"] is not None
        assert game["type"] is not None

def test_create_game_session(game_service):
    # Create a game session
    session = game_service.create_game_session(
        game_name="Magic 8 Ball",
        game_type="fortune_telling",
        players=["Alice"]
    )
    # Verify that the session is created correctly
    assert session["game_name"] == "Magic 8 Ball"
    assert session["players"] == ["Alice"]
    assert session["is_active"] is True
    assert session["session_id"] is not None
    assert session is not None

def test_get_session_by_id(game_service):
    # Create a game session
    session = game_service.create_game_session(
        game_name="Hangman",
        game_type="guessing",
        players=["Bob"]
    )
    session_id = session["session_id"]
    # Retrieve the session by ID
    retrieved_session = game_service.get_session_by_id(session_id)
    # Verify that the session is retrieved correctly
    assert retrieved_session is not None
    assert retrieved_session["session_id"] == session_id
    assert retrieved_session["game_name"] == "Hangman"
    assert retrieved_session["players"] == ["Bob"]
    assert retrieved_session["is_active"] is True

def test_get_nonexistent_session(game_service):
    # Attempt to retrieve a non-existent session
    session = game_service.get_session_by_id("nonexistent-session-id")
    # Verify that None is returned
    assert session is None

def test_make_move_updates_state(game_service):
    # Create a game session
    session = game_service.create_game_session(
        game_name="Hangman",
        game_type="guessing",
        players=["Charlie"]
    )
    session_id = session["session_id"]
    # Make a move in the game session
    game_service.make_move(session_id, {"guessed_letter": "e"})
    # Retrieve the updated session
    updated_session = game_service.get_session_by_id(session_id)
    # Verify that the state is updated correctly
    assert "guessed_letter" in updated_session["state"]
    assert updated_session["state"] == {"guessed_letter": "e"}

def test_make_move_on_nonexistent_session(game_service):
    # Attempt to make a move on a non-existent session
    result = game_service.make_move("nonexistent-session-id", {"guessed_letter": "e"})
    # Verify that None is returned
    assert result is None

def test_end_game_session(game_service):
    # Create a game session
    session = game_service.create_game_session(
        game_name="Bagels",
        game_type="guessing",
        players=["Dana"]
    )
    session_id = session["session_id"]
    # End the game session with a result
    game_service.end_game_session(session_id, result="quit")
    # Retrieve the ended session
    ended_session = game_service.get_session_by_id(session_id)
    # Verify that the session is marked as completed
    assert ended_session["is_completed"] is True
    assert ended_session["is_active"] is False
    assert ended_session["result"] == "quit"
