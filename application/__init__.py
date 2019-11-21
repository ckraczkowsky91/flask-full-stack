# Creating the main module
from flask import Flask

# Instantiating a Flask application object
app = Flask(__name__)

# Creating some default routes
@app.route('/')
@app.route('/index')
@app.route('/barf')
def index():
    return '<h1>Hiyee again!</h1><h2>Hello</h2><p>Hi</p>'
