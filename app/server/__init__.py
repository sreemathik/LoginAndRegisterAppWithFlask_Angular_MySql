import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from app.server.config import Config

static_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, static_folder=static_folder_path)
CORS(app)

app.config.from_object(Config)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from app.server import routes