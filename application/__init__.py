# Creating the main module
from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

# Instantiating a Flask application object
app = Flask(__name__)
app.config.from_object(Config)

# set database equal to mongoengine
db = MongoEngine()
db.init_app(app)

# Import routes
from application import routes
