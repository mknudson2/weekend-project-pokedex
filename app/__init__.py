from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from Config import Config
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app)

login_manager = LoginManager(app)
login_manager.login_view='auth.sign_in'
login_manager.login_message = 'Please log in'
login_manager.login_message_category = 'warning'

from app.blueprints.social import bp as social
app.register_blueprint(social)
from app.blueprints.auth import bp as auth
app.register_blueprint(auth)
from app.blueprints.main import bp as main
app.register_blueprint(main)
from app.blueprints.api import bp as api
app.register_blueprint(api)

from app import models
from app import get_pokemon