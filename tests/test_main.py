from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_hello_user():
    response = client.get('/hello/reza')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello mr reza"}


def test_bye_user():
    response = client.get('/bye/reza/qom')
    assert response.status_code == 200
    assert response.json() == {"message": "goodbye mr reza from qom"}
