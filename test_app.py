import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_create_user(client):
    response = client.post('/users', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'User created successfully'

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(json.loads(response.data), list)

def test_get_user(client):
    # First, create a user
    client.post('/users', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    # Now, retrieve the user
    response = client.get('/users/1')
    assert response.status_code == 200
    user = json.loads(response.data)
    assert user['id'] == 1
    assert user['name'] == 'John Doe'
    assert user['email'] == 'john.doe@example.com'

def test_update_user(client):
    # First, create a user
    client.post('/users', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    # Now, update the user
    response = client.put('/users/1', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'User updated successfully'

def test_delete_user(client):
    # First, create a user
    client.post('/users', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    # Now, delete the user
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'User deleted successfully'
