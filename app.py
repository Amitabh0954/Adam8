import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(f'backend.config.config.{config_name.capitalize()}Config')
    
    db.init_app(app)

    from backend.controllers.auth.registration_controller import registration_bp
    app.register_blueprint(registration_bp, url_prefix='/api/v1/auth')

    return app

if __name__ == '__main__':
    config_name = os.getenv('FLASK_CONFIG', 'development')
    app = create_app(config_name)
    app.run()
```