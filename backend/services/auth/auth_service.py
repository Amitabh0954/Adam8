from datetime import datetime, timedelta
from typing import Optional
import jwt
from backend.models.user_model import User
from backend.repositories.user_repository import UserRepository

class AuthService:
    SECRET_KEY = "YourSecretKey"
    JWT_ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    @staticmethod
    def authenticate_user(email: str, password: str) -> Optional[str]:
        user = UserRepository.get_user_by_email(email)
        if user and user.check_password(password):
            access_token_expires = timedelta(minutes=AuthService.ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = AuthService.create_access_token(
                data={"user_id": user.id}, expires_delta=access_token_expires
            )
            return access_token
        return None

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, AuthService.SECRET_KEY, algorithm=AuthService.JWT_ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_token(token: str) -> Optional[int]:
        try:
            payload = jwt.decode(token, AuthService.SECRET_KEY, algorithms=[AuthService.JWT_ALGORITHM])
            return payload.get("user_id")
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
        return None