import json
from flask import url_for
from backend import create_app, db
from backend.models.user_model import User

app = create_app("testing")

def test_login_user(client):
    user = User(username='testuser', email='test@example.com', password='Password123')
    user.set_password('Password123')
    db.session.add(user)
    db.session.commit()
    url = url_for('login_bp.login')
    data = {
        'email': 'test@example.com',
        'password': 'Password123'
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert 'access_token' in response.json

def test_login_user_with_invalid_credentials(client):
    url = url_for('login_bp.login')
    data = {
        'email': 'invalid@example.com',
        'password': 'invalid'
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 401
    assert response.json['message'] == 'Invalid email or password'