import json
from flask import url_for
from flask_jwt_extended import create_access_token
from backend import create_app, db
from backend.models.user_model import User

app = create_app("testing")

def test_update_profile(client):
    user = User(username='testuser', email='test@example.com', password='Password123')
    db.session.add(user)
    db.session.commit()
    token = create_access_token(identity=user.id)
    headers = {'Authorization': f'Bearer {token}'}
    url = url_for('profile_bp.update_profile')
    data = {
        'username': 'updateduser',
        'email': 'updated@example.com'
    }
    response = client.put(url, data=json.dumps(data), headers=headers, content_type='application/json')

    assert response.status_code == 200
    assert response.json['user']['username'] == 'updateduser'
    assert response.json['user']['email'] == 'updated@example.com'

def test_update_profile_with_existing_email(client):
    user = User(username='testuser', email='test@example.com', password='Password123')
    another_user = User(username='anotheruser', email='another@example.com', password='Password123')
    db.session.add(user)
    db.session.add(another_user)
    db.session.commit()
    token = create_access_token(identity=user.id)
    headers = {'Authorization': f'Bearer {token}'}
    url = url_for('profile_bp.update_profile')
    data = {
        'email': 'another@example.com'
    }
    response = client.put(url, data=json.dumps(data), headers=headers, content_type='application/json')

    assert response.status_code == 400
    assert response.json['message'] == 'Email must be unique'