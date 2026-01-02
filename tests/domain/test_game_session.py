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