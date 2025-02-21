import json
from app import app

def test_create_user():
    tester = app.test_client()
    response = tester.post('/users', json={
        'name': 'KishorMalakar',
        'email': 'kishorMal.com'
    })
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'User created successfully'

def test_get_users():
    tester = app.test_client()
    response = tester.get('/users')
    assert response.status_code == 200
    assert isinstance(json.loads(response.data), list)

def test_get_user():
    tester = app.test_client()
    response = tester.get('/users/1')
    assert response.status_code == 200
    user = json.loads(response.data)
    assert user['id'] == 1
    assert user['name'] == 'KishorMalakar'
    assert user['email'] == 'kishorMal.com'
