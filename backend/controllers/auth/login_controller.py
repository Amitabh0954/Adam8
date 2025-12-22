from flask import Blueprint, request, jsonify
from backend.services.auth.auth_service import AuthService

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400
    token = AuthService.authenticate_user(email, password)
    if token:
        return jsonify({'message': 'Login successful', 'access_token': token}), 200
    return jsonify({'message': 'Invalid email or password'}), 401