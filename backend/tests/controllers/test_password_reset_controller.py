import json
from flask import url_for
from backend import create_app, db
from backend.models.user_model import User
from backend.models.token_model import Token

app = create_app("testing")

def test_request_password_reset(client):
    user = User(username='testuser', email='test@example.com', password='Password123')
    db.session.add(user)
    db.session.commit()
    url = url_for('password_reset_bp.request_password_reset')
    data = {
        'email': 'test@example.com'
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.json['message'] == 'Password reset instructions sent to your email'

def test_reset_password(client):
    user = User(username='testuser', email='test@example.com', password='Password123')
    db.session.add(user)
    db.session.commit()
    token = Token(user_id=user.id, token='validtoken', expires_at=datetime.utcnow() + timedelta(hours=24))
    db.session.add(token)
    db.session.commit()
    url = url_for('password_reset_bp.reset_password')
    data = {
        'token': 'validtoken',
        'new_password': 'NewPassword123'
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.json['message'] == 'Password reset successfully'

def test_reset_password_with_invalid_token(client):
    url = url_for('password_reset_bp.reset_password')
    data = {
        'token': 'invalidtoken',
        'new_password': 'NewPassword123'
    }
    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json['message'] == 'Invalid or expired token'