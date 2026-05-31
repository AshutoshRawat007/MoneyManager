# backend/core/db.py
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the database and serialization libraries
db = SQLAlchemy()
ma = Marshmallow()