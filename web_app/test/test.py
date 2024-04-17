import pytest
from web_app.app import app as flask_app
from web_app.app import db

@pytest.fixture
def app():
    """Configure the app for testing."""
    # Setup your test app configuration here
    flask_app.config.update({
        'TESTING': True,
        'DATABASE_URI': 'mongodb://mongo:27017/test_database'
    })

    # You might need to setup a separate test database here

    yield flask_app  # Use the app for testing

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_home_page(client):
    """Test the home page route."""
    response = client.get('/')
    assert response.status_code == 200

def test_audio_route_get(client):
    """Test the GET request on the audio route."""
    response = client.get('/audio')
    assert response.status_code == 200
    

