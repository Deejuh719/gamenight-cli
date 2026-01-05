# tests/api/test_game_api.py
import pytest
from app import create_app

# Test that the app lists games, creates a session, gets session id and makes a move in the session
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_game_list(client):
    # Test for TC-GN-API-006: List Available Games
    response = client.get('/api/games')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 7 # Current list of games is 7

    # Verify structure of game data
    for game in data:
        assert 'name' in game
        assert 'game_type' in game
        assert 'min_players' in game
        assert 'max_players' in game

def test_create_session(client):
    # Test for TC-GN-API-007: Create Game Session Endpoint
    response = client.post('/api/games/sessions', json={
        "game_type": "fortune_telling",
        "players": ["Alice"]
    })
    data = response.get_json()

    assert response.status_code == 201
    assert data['session_id'] is not None
    assert data['game_type'] == "fortune_telling"
    assert "Alice" in data['players']
    assert data['is_active'] is True

def test_create_session_missing_fields(client):
    # Create Game Session with Missing Fields
    response = client.post('/api/games/sessions', json={})
    data = response.get_json()

    assert response.status_code == 400
    assert 'error' in data

def test_get_session(client):
    # Test for TC-GN-API-008: Get Game Session Endpoint
    # Create Game Session
    response = client.post('/api/games/sessions', json={
        "game_type": "fortune_telling",
        "players": ["Alice"]
    })
    data = response.get_json()
    session_id = data['session_id']

    # Retrieve Game Session
    response = client.get(f'/api/games/sessions/{session_id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data['session_id'] == session_id
    assert data['game_type'] == "fortune_telling"
    assert "Alice" in data['players']
    assert data['is_active'] is True

def test_nonexistent_session(client):
    # Test for TC-GN-API-008: Handle Non-Existent Game Session
    response = client.get('/api/games/sessions/nonexistent-session-id')
    data = response.get_json()

    assert response.status_code == 404
    assert 'error' in data

def test_make_move(client):
    # Test for TC-GN-API-009: Make Move Endpoint
    # Create Game Session
    response = client.post('/api/games/sessions', json={
        "game_type": "fortune_telling",
        "players": ["Alice"]
    })
    data = response.get_json()
    session_id = data['session_id']

    # Make Move
    response = client.post(f'/api/games/sessions/{session_id}/moves', json={
        "player": "Alice",
        "move": "question"
    })
    data = response.get_json()

    assert response.status_code == 201
    assert data['player'] == "Alice"
    assert data['move'] == "question"
    assert data['session_id'] == session_id

def test_make_move_invalid_data(client):
    # Test for TC-GN-API-009: Handle Invalid Move Data
    # Create Game Session
    response = client.post('/api/games/sessions', json={
        "game_type": "fortune_telling",
        "players": ["Alice"]
    })
    data = response.get_json()
    session_id = data['session_id']

    # Make Move with Invalid Data
    response = client.post(f'/api/games/sessions/{session_id}/moves', json={})
    data = response.get_json()

    assert response.status_code == 400
    assert 'error' in data

