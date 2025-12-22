from datetime import datetime
from typing import Optional
from backend.models.token_model import Token
from backend import db

class TokenRepository:

    @staticmethod
    def save_token(user_id: int, token: str, expires_at: datetime) -> None:
        token_instance = Token(user_id=user_id, token=token, expires_at=expires_at)
        db.session.add(token_instance)
        db.session.commit()

    @staticmethod
    def get_token(token: str) -> Optional[Token]:
        return Token.query.filter_by(token=token).first()

    @staticmethod
    def delete_token(token: str) -> None:
        token_instance = Token.query.filter_by(token=token).first()
        if token_instance:
            db.session.delete(token_instance)
            db.session.commit()