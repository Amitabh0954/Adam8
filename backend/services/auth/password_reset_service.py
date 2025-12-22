import uuid
from datetime import datetime, timedelta
from backend.models.user_model import User
from backend.repositories.user_repository import UserRepository
from backend.repositories.token_repository import TokenRepository
from backend.integrations.email_service import EmailService
from backend import db

class PasswordResetService:
    @staticmethod
    def request_password_reset(email: str) -> None:
        user = UserRepository.get_user_by_email(email)
        if not user:
            raise ValueError("User does not exist")

        token = str(uuid.uuid4())
        expires_at = datetime.utcnow() + timedelta(hours=24)
        TokenRepository.save_token(user.id, token, expires_at)

        reset_link = f"https://yourdomain.com/reset-password?token={token}"
        EmailService.send_email(user.email, "Password Reset Request", f"Click the link to reset your password: {reset_link}")

    @staticmethod
    def reset_password(token: str, new_password: str) -> None:
        token_data = TokenRepository.get_token(token)
        if not token_data or token_data.expires_at < datetime.utcnow():
            raise ValueError("Invalid or expired token")

        user = UserRepository.get_user_by_id(token_data.user_id)
        if not user:
            raise ValueError("User does not exist")

        user.set_password(new_password)
        UserRepository.update_user()
        TokenRepository.delete_token(token)