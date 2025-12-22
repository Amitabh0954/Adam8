from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(20), unique=True, nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    image_file: str = db.Column(db.String(20), nullable=False, default='default.jpg')
    password: str = db.Column(db.String(60), nullable=False)
    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password, password)

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    with app.app_context():
        db.create_all()