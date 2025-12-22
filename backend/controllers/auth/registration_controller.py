from flask import Blueprint, request, jsonify
from backend.services.auth.registration_service import RegistrationService

registration_bp = Blueprint('registration_bp', __name__)

@registration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({'message': 'All fields are required'}), 400
    try:
        user = RegistrationService.register_user(username, email, password)
        return jsonify({'message': 'User registered successfully', 'user': {'id': user.id, 'username': user.username, 'email': user.email}}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400