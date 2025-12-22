from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.services.auth.profile_service import ProfileService

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    
    try:
        user = ProfileService.update_profile(user_id, username, email)
        return jsonify({'message': 'Profile updated successfully', 'user': {'id': user.id, 'username': user.username, 'email': user.email}}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400