# tests/services/test_game_service.py
import pytest
from app.services.game_service import GameService
from app.domain.game_session import GameSession

"""
Focuses on tests GN-SRV-001 and GN-SRV-002
Assuring that GameService will list available games
and create new game sessions correctly.
"""
@pytest.fixture
def game_service():
    return GameService()

def test_list_available_games(game_service):
    available_games = game_service.list_available_games()
    assert isinstance(available_games, list)
    assert len(available_games) > 0
    assert available_games[0]["name"] == "Magic 8 Ball"
    assert available_games[1]["name"] == "Blackjack"
    assert available_games[2]["name"] == "Hangman"

def test_create_game_session(game_service):
    game_session = game_service.create_game_session("Hangman")
    assert isinstance(game_session, GameSession)
    assert game_session.name == "Hangman"
    assert game_session.status == "active"
    assert game_session.state == {}


def test_get_game_session_by_id(game_service):
    game_session = game_service.create_game_session("Hangman")
    retrieved_game_session = game_service.get_game_session_by_id(game_session.id)
    assert retrieved_game_session == game_session

def test_get_game_session_by_invalid_id(game_service):
    retrieved_game_session = game_service.get_game_session_by_id("non-existent-id")
    assert retrieved_game_session is None

def test_multiple_game_sessions(game_service):
    game_session1 = game_service.create_game_session("Hangman")
    game_session2 = game_service.create_game_session("Blackjack")
    assert game_session1.id != game_session2.id

def test_game_move_updates_state(game_service):
    game_session = game_service.create_game_session("Hangman")
    game_service.game_move(game_session.id, {"guess": "a"})
    assert game_session.state == {"guess": "a"}
    game_service.game_move(game_session.id, {"guess": "b"})
    assert game_session.state == {"guess": "b"}

def test_game_move_invalid_session(game_service):
    with pytest.raises(KeyError):
        game_service.game_move("non-existent-id", {"guess": "a"})