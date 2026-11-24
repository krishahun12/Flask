"""Automated unit tests for the Flask application."""

import pytest
from app import app


@pytest.fixture
def client():
    """Create a Flask test client configured for testing."""
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_hello_world(client):
    """Verify that GET / returns HTTP 200 and 'Hello, World!'."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, World!"
