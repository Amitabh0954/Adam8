import json
from flask import url_for
from backend import create_app, db
from backend.models.user_model import User

app = create_app("testing")

def test_register_user(client):
    url = url_for('registration_bp.register')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'Password123'
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 201
    assert response.json['user']['username'] == 'testuser'
    assert response.json['user']['email'] == 'test@example.com'

def test_register_user_with_existing_email(client):
    user = User(username='existinguser', email='existing@example.com', password='Password123')
    db.session.add(user)
    db.session.commit()
    url = url_for('registration_bp.register')
    data = {
        'username': 'testuser',
        'email': 'existing@example.com',
        'password': 'Password123'
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json['message'] == 'Email must be unique'

def test_register_user_with_weak_password(client):
    url = url_for('registration_bp.register')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password'
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json['message'] == 'Password must meet security criteria'