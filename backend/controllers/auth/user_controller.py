from flask import Blueprint, request, jsonify, session
from backend.services.auth.user_service import UserService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        user = UserService.register_user(data['username'], data['email'], data['password'])
        response = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'image_file': user.image_file,
            'created_at': user.created_at.isoformat()
        }
        return jsonify(response), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        user = UserService.authenticate_user(data['email'], data['password'])
        session.clear()
        session['user_id'] = user.id
        session.modified = True
        response = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'image_file': user.image_file,
            'created_at': user.created_at.isoformat()
        }
        return jsonify(response), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 401