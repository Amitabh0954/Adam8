from flask import Flask, session
from backend.config.config import config
from backend.models.user import init_db
from backend.controllers.auth.user_controller import auth_bp

# Initialize Flask app
app = Flask(__name__)

# Load Config
app.config.from_object(config)

# Initialize DB
init_db(app)

# Session Management
app.config['SESSION_COOKIE_NAME'] = config.SESSION_COOKIE_NAME
app.config['PERMANENT_SESSION_LIFETIME'] = config.PERMANENT_SESSION_LIFETIME

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.before_request
def make_session_permanent():
    session.permanent = True

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=config.LOGGING_LEVEL)
    app.run(host='0.0.0.0', port=5000)