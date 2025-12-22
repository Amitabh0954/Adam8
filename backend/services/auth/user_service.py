from backend.repositories.user_repository import UserRepository
from backend.models.user import User

class UserService:
    login_attempts_cache = {}

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
        if email in UserService.login_attempts_cache and UserService.login_attempts_cache[email] >= 5:
            raise ValueError("Too many invalid login attempts. Please try again later.")
        
        user = UserRepository.get_user_by_email(email)
        if user and user.check_password(password):
            UserService.reset_login_attempts(email)
            return user
        
        UserService.increment_login_attempts(email)
        raise ValueError("Invalid credentials")

    @staticmethod
    def increment_login_attempts(email: str) -> None:
        if email not in UserService.login_attempts_cache:
            UserService.login_attempts_cache[email] = 0
        UserService.login_attempts_cache[email] += 1

    @staticmethod
    def reset_login_attempts(email: str) -> None:
        if email in UserService.login_attempts_cache:
            UserService.login_attempts_cache[email] = 0