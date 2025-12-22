from backend.repositories.user_repository import UserRepository
from backend.models.user import User

class UserService:
    @staticmethod
    def register_user(username: str, email: str, password: str) -> User:
        if UserRepository.get_user_by_email(email) or UserRepository.get_user_by_username(username):
            raise ValueError("Email or username already exists")
        
        hashed_password = User.hash_password(password)
        user = User(username=username, email=email, password=hashed_password)
        UserRepository.save_user(user)
        return user
    
    @staticmethod
    def authenticate_user(email: str, password: str) -> User:
        user = UserRepository.get_user_by_email(email)
        if user and user.check_password(password):
            return user
        raise ValueError("Invalid credentials")