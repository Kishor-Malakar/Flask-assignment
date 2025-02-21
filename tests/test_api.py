import requests

BASE_URL = "http://localhost:5000"

def test_create_user():
    response = requests.post(f"{BASE_URL}/users", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
