from typing import Optional
from backend.models.user_model import User
from backend import db

class UserRepository:

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_user_by_email(email: str) -> Optional[User]:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def add_user(user: User) -> None:
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update_user() -> None:
        db.session.commit()

    @staticmethod
    def delete_user(user: User) -> None:
        db.session.delete(user)
        db.session.commit()