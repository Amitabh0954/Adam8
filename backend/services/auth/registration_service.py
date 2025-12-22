from typing import Dict
from backend.models.user_model import User
from backend.repositories.user_repository import UserRepository

class RegistrationService:
    @staticmethod
    def register_user(username: str, email: str, password: str) -> User:
        if UserRepository.get_user_by_email(email):
            raise ValueError("Email must be unique")
        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password) or not any(char.islower() for char in password):
            raise ValueError("Password must meet security criteria")
        user = User(username=username, email=email, password=password)
        UserRepository.add_user(user)
        return user