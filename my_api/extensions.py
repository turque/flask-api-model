# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from passlib.context import CryptContext

from my_api.commons.apispec import APISpecExt

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()
apispec = APISpecExt()
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
