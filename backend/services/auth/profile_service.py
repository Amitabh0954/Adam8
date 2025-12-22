from typing import Optional
from backend.models.user_model import User
from backend.repositories.user_repository import UserRepository

class ProfileService:
    @staticmethod
    def update_profile(user_id: int, username: Optional[str] = None, email: Optional[str] = None) -> User:
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        if username:
            user.username = username
        if email:
            if UserRepository.get_user_by_email(email) and user.email != email:
                raise ValueError("Email must be unique")
            user.email = email
        
        UserRepository.update_user()
        return user