from backend.models.user import User, db

class UserRepository:
    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_email(email: str) -> User:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def save_user(user: User) -> None:
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def delete_user(user: User) -> None:
        db.session.delete(user)
        db.session.commit()