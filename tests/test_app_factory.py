from app import create_app
from flask import Flask


def test_create_app_returns_flask_instance():
    app = create_app()
    assert isinstance(app, Flask)


def test_app_returns_404_when_no_route_defined():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 404
