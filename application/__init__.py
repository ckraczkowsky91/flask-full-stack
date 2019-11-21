# Creating the main module
from flask import Flask

# Instantiating a Flask application object
app = Flask(__name__)

# Import routes
from application import routes
