from flask import Blueprint, request, jsonify
from backend.services.auth.password_reset_service import PasswordResetService

password_reset_bp = Blueprint('password_reset_bp', __name__)

@password_reset_bp.route('/password-reset/request', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({'message': 'Email is required'}), 400
    try:
        PasswordResetService.request_password_reset(email)
        return jsonify({'message': 'Password reset instructions sent to your email'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@password_reset_bp.route('/password-reset/reset', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')
    if not token or not new_password:
        return jsonify({'message': 'Token and new password are required'}), 400
    try:
        PasswordResetService.reset_password(token, new_password)
        return jsonify({'message': 'Password reset successfully'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400